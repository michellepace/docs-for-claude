#!/usr/bin/env python3
"""Validate documentation directory INDEX.xml synchronization with markdown files.

Usage:
    python scripts/validate_directory.py <directory>

Example:
    python scripts/validate_directory.py uv
"""

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def get_base_url(url: str) -> str:
    """Remove fragments and trailing slash from URL for comparison."""
    return url.split("\\#")[0].split("#")[0].rstrip("/")


def get_element_text(element: ET.Element | None) -> str:
    """Extract text from XML element, returning empty string if None."""
    return element.text if element is not None and element.text else ""


def initialize_results(directory: str) -> dict:
    """Initialize validation results dictionary."""
    return {
        "directory": directory,
        "xml_valid": False,
        "source_count": 0,
        "files_exist": 0,
        "total_files": 0,
        "orphan_files": [],
        "issues": [],
    }


def parse_index_xml(directory_path: Path, results: dict) -> list | None:
    """Parse and validate INDEX.xml structure, returning source elements."""
    index_path = directory_path / "INDEX.xml"

    if not index_path.exists():
        results["issues"].append(f"❌ ERROR: {index_path} not found")
        return None

    try:
        tree = ET.parse(index_path)
        root = tree.getroot()

        if root.tag != "docs_index":
            results["issues"].append("❌ ERROR: Root must be <docs_index>")
            return None

        sources = root.findall("source")
        results["xml_valid"] = True
        results["source_count"] = len(sources)
    except ET.ParseError as e:
        results["issues"].append(f"❌ ERROR: {index_path} is malformed - {e}")
        return None

    if not sources:
        results["issues"].append("❌ ERROR: INDEX.xml contains no <source> elements")
        return None

    return sources


def validate_source_element(
    idx: int, source: ET.Element, results: dict
) -> tuple[str, str, str, str]:
    """Validate source element fields and return extracted text."""
    title_text = get_element_text(source.find("title"))
    desc_text = get_element_text(source.find("description"))
    url_text = get_element_text(source.find("source_url"))
    file_text = get_element_text(source.find("local_file"))

    required_fields = {
        "title": title_text,
        "description": desc_text,
        "local_file": file_text,
        "source_url": url_text,
    }

    for field_name, field_value in required_fields.items():
        if not field_value:
            results["issues"].append(f"  • Source #{idx}: Empty <{field_name}>")

    if url_text and not url_text.startswith(("http://", "https://")):
        results["issues"].append(f"  • Source #{idx}: Invalid URL protocol '{url_text}'")

    return title_text, desc_text, url_text, file_text


def validate_markdown_file(
    directory_path: Path, file_text: str, title_text: str, url_text: str, results: dict
) -> bool:
    """Validate markdown file exists and first line matches INDEX.xml metadata."""
    file_path = directory_path / file_text

    if not file_path.exists():
        results["issues"].append(f"  • {file_text}: File does not exist")
        return False

    results["files_exist"] += 1

    try:
        with file_path.open(encoding="utf-8") as f:
            first_line = f.readline().strip()
    except (OSError, UnicodeDecodeError) as e:
        results["issues"].append(f"  • {file_text}: Error reading file - {e}")
        return False

    match = re.match(r"#\s*\[([^\]]*)\]\(([^\)]+)\)", first_line)
    if not match:
        results["issues"].append(
            f"  • {file_text}:1 - Invalid first line format (expected '# [Title](URL)')"
        )
        return False

    md_title = match.group(1)
    md_url = match.group(2)

    if md_title != title_text:
        results["issues"].append(
            f"  • {file_text}:1 - Title mismatch: INDEX='{title_text}' vs MD='{md_title}'"
        )

    if get_base_url(md_url) != get_base_url(url_text):
        results["issues"].append(
            f"  • {file_text}:1 - URL mismatch: INDEX='{url_text}' vs MD='{md_url}'"
        )

    return True


def validate_directory(directory: str) -> dict:
    """Validate INDEX.xml structure, file references, and detect orphans."""
    directory_path = Path(directory)
    results = initialize_results(directory)

    sources = parse_index_xml(directory_path, results)
    if not sources:
        return results

    referenced_files = set()
    for idx, source in enumerate(sources, 1):
        title_text, _, url_text, file_text = validate_source_element(idx, source, results)

        if not file_text:
            continue

        referenced_files.add(file_text)
        results["total_files"] += 1

        validate_markdown_file(directory_path, file_text, title_text, url_text, results)

    all_md_files = {p.name for p in directory_path.glob("*.md") if p.name != "README.md"}
    results["orphan_files"] = sorted(all_md_files - referenced_files)

    return results


def print_status(*, is_success: bool, success_msg: str, fail_msg: str) -> None:
    """Print success or failure message with emoji prefix."""
    print(f"{'✅' if is_success else '❌'} {success_msg if is_success else fail_msg}")


def print_report(results: dict) -> int:
    """Print formatted validation report and return exit code."""
    directory = results["directory"]

    print(f"🔍 Validation Report: {directory}/\n")

    if not results["xml_valid"]:
        for issue in results["issues"]:
            print(issue)
        if "not found" in results["issues"][0]:
            print(
                f"\nAdd .md files to {directory}/ then create index manually or "
                "via automation."
            )
        else:
            print(
                "\nCheck for unclosed tags, invalid characters, or missing </docs_index>"
            )
        return 1

    print("INDEX.xml Structure:")
    print("✅ Well-formed XML")
    print(f"✅ {results['source_count']} <source> elements\n")

    print("File Sync:")
    print_status(
        is_success=results["files_exist"] == results["total_files"],
        success_msg=(
            f"All referenced files exist "
            f"({results['files_exist']}/{results['total_files']})"
        ),
        fail_msg=(
            f"Not all referenced files exist "
            f"({results['files_exist']}/{results['total_files']})"
        ),
    )
    print_status(
        is_success=not results["orphan_files"],
        success_msg="No orphan files",
        fail_msg=f"{len(results['orphan_files'])} orphan file(s) found",
    )

    print("\nMetadata Sync:")

    has_title_mismatches = any("Title mismatch" in issue for issue in results["issues"])
    has_url_mismatches = any("URL mismatch" in issue for issue in results["issues"])

    print_status(
        is_success=not has_title_mismatches,
        success_msg="All titles match",
        fail_msg="Title mismatches found",
    )
    print_status(
        is_success=not has_url_mismatches,
        success_msg="All URLs match",
        fail_msg="URL mismatches found",
    )

    if results["issues"] or results["orphan_files"]:
        print("\nIssues:")
        for issue in results["issues"]:
            print(issue)
        for orphan in results["orphan_files"]:
            print(f"  • {orphan}: Orphan file (not in INDEX.xml)")

        total_issues = len(results["issues"]) + len(results["orphan_files"])
        print(f"\nSummary: ⚠️  {total_issues} issue(s) found")
        return 1
    print("\nSummary: ✅ All validations passed")
    return 0


def main() -> None:
    """Parse arguments, validate directory, and exit with status code."""
    required_args = 2
    if len(sys.argv) != required_args:
        print("Usage: uv run scripts/validate_dir.py <directory>", file=sys.stderr)
        sys.exit(1)

    directory = sys.argv[1]
    results = validate_directory(directory)
    exit_code = print_report(results)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
