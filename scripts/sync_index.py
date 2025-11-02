"""Sync INDEX.xml, re-scrape all docs, output results for batch processing."""

import argparse
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def get_markdown_files(collection_dir: Path) -> set[str]:
    """Return set of .md filenames (excluding README.md)."""
    return {file.name for file in collection_dir.glob("*.md") if file.name != "README.md"}


def _sync_index_to_filesystem(
    index_path: Path, md_files: set[str]
) -> tuple[list[tuple[str, str]], list[str], int]:
    """Remove invalid sources from INDEX.xml, write cleaned file, return results.

    Args:
        index_path: Path to INDEX.xml file
        md_files: Set of existing .md filenames

    Returns:
        Tuple of (valid_pairs, orphans, removed_count) where:
        - valid_pairs: List of (local_file, source_url) tuples
        - orphans: List of .md filenames not in INDEX.xml
        - removed_count: Number of invalid sources removed
    """
    tree = ET.parse(index_path)
    root = tree.getroot()

    valid_pairs = []
    indexed_files = set()
    removed_count = 0

    # Process each source entry
    for source in list(root.findall("source")):
        local_file_elem = source.find("local_file")
        source_url_elem = source.find("source_url")

        if local_file_elem is None or source_url_elem is None:
            root.remove(source)
            removed_count += 1
            continue

        local_file = local_file_elem.text
        source_url = source_url_elem.text

        # Remove if markdown file doesn't exist
        if local_file not in md_files:
            root.remove(source)
            removed_count += 1
        else:
            # Valid entry
            valid_pairs.append((local_file, source_url))
            indexed_files.add(local_file)

    # Find orphan markdown files (exist but not in INDEX)
    orphans = sorted(md_files - indexed_files)

    # Write cleaned INDEX.xml back
    if removed_count > 0:
        ET.indent(root, space="  ")
        tree.write(index_path, encoding="unicode", xml_declaration=False)

    return valid_pairs, orphans, removed_count


def _scrape_doc(collection_dir: Path, source_url: str) -> bool:
    """Scrape single doc using curate_doc.py via subprocess.

    Args:
        collection_dir: Collection directory path
        source_url: URL to scrape

    Returns:
        True if successful, False if failed
    """
    # Find uv executable with absolute path to prevent PATH hijacking (S607)
    uv_path = shutil.which("uv")
    if not uv_path:
        print("Error: 'uv' executable not found in PATH", file=sys.stderr)
        return False

    # S603: Subprocess call is safe - calling our own trusted script with validated args
    # - collection_dir is validated by main() to be existing dir with INDEX.xml
    # - source_url is validated by curate_doc.py via urlparse
    # - Using list (not shell=True) prevents command injection
    result = subprocess.run(
        [uv_path, "run", "scripts/curate_doc.py", str(collection_dir), source_url],
        check=False,
        capture_output=False,  # Let output stream through
        text=True,
    )
    return result.returncode == 0


def _print_git_changes_summary(collection_dir: Path) -> None:
    """Print git diff stats for the collection directory.

    Args:
        collection_dir: Path to collection directory
    """
    git_path = shutil.which("git")
    if not git_path:
        print("⚠️  Git not found - skipping change detection")
        return

    # S603: Subprocess call is safe - calling git with validated directory path
    # - collection_dir validated in main() to be existing directory
    # - Using list (not shell=True) prevents command injection
    result = subprocess.run(
        [git_path, "diff", "--stat", "-w", "."],
        check=False,
        capture_output=True,
        text=True,
        cwd=collection_dir,
    )

    if result.stdout.strip():
        print("GIT_CHANGES_START")
        print(result.stdout.rstrip())
        print("GIT_CHANGES_END")
    else:
        print("GIT_CHANGES_START")
        print("No content changes detected")
        print("GIT_CHANGES_END")


def _print_structured_output(
    valid_pairs: list[tuple[str, str]],
    failed_urls: list[str],
    orphans: list[str],
    collection_dir: Path,
) -> None:
    """Print structured output for Claude Code to parse.

    Output format:
        === SCRAPE SUMMARY ===
        SUCCESSFUL: <count>
        FAILED: <count>

        FAILED_URLS_START
        <url1>
        <url2>
        FAILED_URLS_END

        ORPHANS_START
        <collection_dir>/<file1.md>
        <collection_dir>/<file2.md>
        ORPHANS_END

    This format is parsed by .claude/commands/rescrape-docs.md workflow.
    """
    # Scrape summary
    print("=== SCRAPE SUMMARY ===")
    print(f"SUCCESSFUL: {len(valid_pairs) - len(failed_urls)}")
    print(f"FAILED: {len(failed_urls)}")
    print()

    # Failed URLs
    if failed_urls:
        print("FAILED_URLS_START")
        for url in failed_urls:
            print(url)
        print("FAILED_URLS_END")
        print()

    # Orphans
    if orphans:
        print("ORPHANS_START")
        for orphan in orphans:
            print(f"{collection_dir}/{orphan}")
        print("ORPHANS_END")
        print()


def _backup_index_xml(index_path: Path) -> Path:
    """Validate XML structure and create backup file."""
    try:
        ET.parse(index_path)
    except ET.ParseError as e:
        print(f"❌ Error: INVALID_XML|{e}|{index_path}|", file=sys.stderr)
        sys.exit(1)

    backup_path = index_path.with_suffix(".xml.backup")
    shutil.copy2(index_path, backup_path)
    return backup_path


def _get_changed_markdown_files(collection_dir: Path) -> set[str]:
    """Get set of changed .md filenames from git diff (excludes README.md)."""
    git_path = shutil.which("git")
    if not git_path:
        return set()

    result = subprocess.run(
        [git_path, "diff", "--name-only", "-w", "."],
        capture_output=True,
        text=True,
        check=False,
        cwd=collection_dir,
    )

    changed_files = set()
    for line in result.stdout.strip().split("\n"):
        if line.endswith(".md") and not line.endswith("README.md"):
            changed_files.add(Path(line).name)

    return changed_files


def _restore_unchanged_descriptions(
    index_path: Path, backup_path: Path, changed_files: set[str]
) -> int:
    """Restore descriptions for unchanged files from backup."""
    backup_tree = ET.parse(backup_path)
    backup_root = backup_tree.getroot()
    backup_descriptions = {}

    for source in backup_root.findall("source"):
        local_file_elem = source.find("local_file")
        desc_elem = source.find("description")

        if local_file_elem is not None and desc_elem is not None:
            backup_descriptions[local_file_elem.text] = desc_elem.text

    tree = ET.parse(index_path)
    root = tree.getroot()
    restored_count = 0

    for source in root.findall("source"):
        local_file_elem = source.find("local_file")
        desc_elem = source.find("description")

        if local_file_elem is None or desc_elem is None:
            continue

        local_file = local_file_elem.text

        if (
            local_file not in changed_files
            and local_file in backup_descriptions
            and backup_descriptions[local_file] != "PLACEHOLDER"
        ):
            desc_elem.text = backup_descriptions[local_file]
            restored_count += 1

    if restored_count > 0:
        ET.indent(root, space="  ")
        tree.write(index_path, encoding="unicode", xml_declaration=False)

    return restored_count


def _cleanup_backup(backup_path: Path) -> None:
    """Delete backup file with error handling (non-fatal)."""
    try:
        backup_path.unlink(missing_ok=True)
    except OSError as e:
        print(f"⚠️  Could not delete backup: {e}", file=sys.stderr)


def main() -> None:
    """Sync INDEX.xml, scrape all docs, output structured results."""
    parser = argparse.ArgumentParser(
        description="Sync INDEX.xml, re-scrape all docs, output batch processing data"
    )
    parser.add_argument("directory", help="Collection directory (e.g. shiny/)")
    args = parser.parse_args()

    collection_dir = Path(args.directory)
    index_path = collection_dir / "INDEX.xml"

    # Validate directory and INDEX.xml exist
    if not collection_dir.exists() or not collection_dir.is_dir():
        print(f"Error: Directory '{collection_dir}' does not exist", file=sys.stderr)
        sys.exit(1)

    if not index_path.exists():
        print(f"Error: INDEX.xml not found in '{collection_dir}'", file=sys.stderr)
        sys.exit(1)

    # Backup INDEX.xml (validates XML structure)
    backup_path = _backup_index_xml(index_path)

    # Step 1: Sync INDEX.xml
    md_files = get_markdown_files(collection_dir)
    valid_pairs, orphans, removed_count = _sync_index_to_filesystem(index_path, md_files)

    print("=== SYNC COMPLETE ===")
    print(f"REMOVED_SOURCES: {removed_count}")
    print(f"VALID_DOCS: {len(valid_pairs)}")
    print()

    # Step 2: Scrape all docs
    print("=== SCRAPING ALL DOCS ===")
    failed_urls = []

    for idx, (local_file, source_url) in enumerate(valid_pairs, 1):
        print(f"## 🔄 Doc {idx} of {len(valid_pairs)}: {local_file}")
        success = _scrape_doc(collection_dir, source_url)

        if success:
            print("✅ Success")
        else:
            print("❌ Failed")
            failed_urls.append(source_url)
        print()

    # Step 3: Output structured results
    _print_structured_output(valid_pairs, failed_urls, orphans, collection_dir)

    # Step 4: Show git changes summary
    print()
    _print_git_changes_summary(collection_dir)

    # Restore unchanged descriptions
    changed_files = _get_changed_markdown_files(collection_dir)
    restored_count = _restore_unchanged_descriptions(
        index_path, backup_path, changed_files
    )
    print(f"📝 Restored {restored_count} unchanged description(s)")

    # Cleanup backup file
    _cleanup_backup(backup_path)


if __name__ == "__main__":
    main()
