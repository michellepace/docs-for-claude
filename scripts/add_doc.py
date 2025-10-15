"""Deterministic tasks for `/add-doc` command, prints actionable info."""

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from datetime import date
from os import environ
from pathlib import Path
from urllib.parse import urlparse

from firecrawl import Firecrawl


def normalise_directory_path(path_str: str) -> Path:
    """Normalise directory path by removing trailing slash."""
    return Path(path_str.rstrip("/"))


def validate_url(url: str) -> None:
    """Validate URL has scheme and netloc, exit if invalid."""
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        print(f"Error: ❌ '{url}' is not a valid URL", file=sys.stderr)
        sys.exit(1)


def validate_directory(dir_path: Path, index_path: Path) -> None:
    """Validate directory is suitable for docs collection, exit if invalid."""
    if dir_path.exists() and not index_path.exists() and any(dir_path.iterdir()):
        print(
            f"Error: ❌ Directory '{dir_path}' is not empty and "
            f"missing INDEX.xml. Use an empty directory or a valid docs collection.",
            file=sys.stderr,
        )
        sys.exit(1)


def slugify_title(title: str) -> str:
    """Convert title to filename-safe slug."""
    slug = title.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[-\s]+", "-", slug)
    return slug.strip("-")


def create_readme(dir_path: Path, dir_name: str, source_url: str) -> None:
    """Create README.md for new directory."""
    readme_content = f"""# {dir_name} Documentation

Curated docs for targeted AI context.

- Curation Index: [INDEX.xml](INDEX.xml)
- Curation Source: <{source_url}>
"""
    readme_path = dir_path / "README.md"
    readme_path.write_text(readme_content)
    print(f"✅ Successfully added {readme_path}")


def create_index_xml(dir_path: Path) -> None:
    """Create empty INDEX.xml structure."""
    root = ET.Element("docs_index")
    ET.indent(root, space="  ")

    tree = ET.ElementTree(root)
    index_path = dir_path / "INDEX.xml"
    tree.write(index_path, encoding="unicode", xml_declaration=False)
    print(f"✅ Created empty INDEX.xml at {index_path}")


def add_or_update_source_in_index(
    dir_path: Path, title: str, source_url: str, local_file: str
) -> tuple[bool, Path | None]:
    """Add new source or update existing source in INDEX.xml.

    Returns:
        (is_update, old_file_path): is_update=True if updating existing source,
                                     old_file_path=Path to previous file if different
    """
    index_path = dir_path / "INDEX.xml"

    # Parse existing XML
    tree = ET.parse(index_path)
    root = tree.getroot()

    is_update = False
    old_filename = None

    # Check for existing source with same URL
    for existing_source in root.findall("source"):
        existing_url_elem = existing_source.find("source_url")
        if existing_url_elem is not None and existing_url_elem.text == source_url:
            # Found duplicate - capture old filename for cleanup
            old_file_elem = existing_source.find("local_file")
            if old_file_elem is not None:
                old_filename = old_file_elem.text

            # Delete old source entry
            root.remove(existing_source)
            is_update = True
            print(f"💡 Updating existing source for: {source_url}")
            break

    # Add new source entry (whether new or replacing old)
    source = ET.SubElement(root, "source")
    ET.SubElement(source, "title").text = title
    ET.SubElement(source, "description").text = "PLACEHOLDER"
    ET.SubElement(source, "source_url").text = source_url
    ET.SubElement(source, "local_file").text = local_file
    ET.SubElement(source, "scraped_at").text = date.today().isoformat()

    # Re-indent entire tree for pretty printing
    ET.indent(root, space="  ")

    # Write back to file
    tree.write(index_path, encoding="unicode", xml_declaration=False)

    action = "Updated" if is_update else "Added new"
    print(f"✅ {action} <source> to INDEX.xml with local_file: {local_file}")

    # Return Path object for cleanup (if filename changed)
    old_file_path = (
        (dir_path / old_filename) if old_filename and old_filename != local_file else None
    )
    return is_update, old_file_path


def cleanup_old_file(old_file_path: Path | None) -> None:
    """Delete old markdown file if filename changed during update.

    Args:
        old_file_path: Path to previous file to remove (or None if no cleanup needed)
    """
    if old_file_path:
        old_file_path.unlink(missing_ok=True)
        print(f"🗑️  Removed old file: {old_file_path.name}")


def scrape_with_firecrawl(url: str) -> dict:
    """Scrape URL using FireCrawl Python SDK.

    Returns dict with:
    - markdown: str (content)
    - metadata: dict (title)

    Raises:
    - SystemExit(1) on errors (prints to stderr)
    """
    api_key = environ.get("API_KEY_MCP_FIRECRAWL")
    if not api_key:
        print("Error: ❌ API_KEY_MCP_FIRECRAWL not set", file=sys.stderr)
        sys.exit(1)

    try:
        firecrawl = Firecrawl(api_key=api_key)
        result = firecrawl.scrape(
            url,
            formats=["markdown"],
            only_main_content=True,
            remove_base64_images=True,
            wait_for=2000,
            max_age=172800000,
        )

        # Validate result (it's a Document object with attributes)
        if not result or not hasattr(result, "markdown") or not result.markdown:
            print(
                f"Error: ❌ Failed to scrape '{url}' - no content returned",
                file=sys.stderr,
            )
            sys.exit(1)
        else:
            # Extract metadata attributes
            metadata = {}
            if hasattr(result, "metadata") and result.metadata:
                metadata = {
                    "title": getattr(result.metadata, "title", "Untitled"),
                }

            return {
                "markdown": result.markdown,
                "metadata": metadata,
            }

    except (OSError, ValueError, RuntimeError) as e:
        print(f"Error: ❌ Failed to scrape '{url}': {e}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    """Parse arguments and process documentation."""
    parser = argparse.ArgumentParser(
        description="Deterministic tasks for `/add-doc` command, prints actionable info"
    )

    parser.add_argument("directory", help="Documentation directory (e.g. `tailwind/`)")
    parser.add_argument("source_url", help="Web URL to scrape and add new document from")

    args = parser.parse_args()

    validate_url(args.source_url)

    dir_path = normalise_directory_path(args.directory)
    index_path = dir_path / "INDEX.xml"
    validate_directory(dir_path, index_path)

    # Ensure directory exists
    dir_path.mkdir(parents=True, exist_ok=True)

    # Scrape with FireCrawl (do this before creating files to fail fast)
    scraped_doc = scrape_with_firecrawl(args.source_url)
    content = scraped_doc["markdown"]
    metadata = scraped_doc["metadata"]
    title = metadata.get("title", "Untitled")

    # Extract base URL (scheme + netloc) for README collection source
    parsed_url = urlparse(args.source_url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

    # Create README and INDEX if new collection
    if not index_path.exists():
        create_readme(dir_path, dir_path.name, base_url)
        create_index_xml(dir_path)

    # Generate filename from title
    filename = f"{slugify_title(title)}.md"
    file_path = dir_path / filename

    # Write markdown file (overwrites if exists)
    file_path.write_text(content)

    # Update INDEX.xml (add or update)
    is_update, old_file_path = add_or_update_source_in_index(
        dir_path, title, args.source_url, filename
    )

    # Cleanup old .md file if filename changed
    cleanup_old_file(old_file_path)

    # Print final success message
    action = "Re-scraped and updated" if is_update else "Successfully added and indexed"
    print(f"{'♻️' if is_update else '✅'} {action}: {filename}")


if __name__ == "__main__":
    main()
