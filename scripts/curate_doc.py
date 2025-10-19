"""Add or update documentation in collection directories by scraping URLs.

Scrapes web pages using Firecrawl, manages INDEX.xml metadata, and handles
duplicate titles, rate limits, and file cleanup.
"""

import argparse
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import date
from os import environ
from pathlib import Path
from urllib.parse import urlparse

from firecrawl import Firecrawl
from firecrawl.v2.types import Document
from firecrawl.v2.utils.error_handler import FirecrawlError, RateLimitError


def _normalise_directory_path(dir_path_str: str) -> Path:
    """Normalise directory path by removing trailing slash."""
    return Path(dir_path_str.rstrip("/"))


def _format_path_for_display(path: Path) -> str:
    """Format path as relative-to-project for consistent display.

    Converts any Path object to a clean relative path string for printing.
    Ensures consistent output regardless of whether input paths are absolute,
    relative, or use ./ notation.

    Args:
        path: Path object to format (can be absolute or relative)

    Returns:
        String representation relative to project root (e.g., "vite/INDEX.xml")

    Examples:
        Path("/home/mp/.../vite/README.md") → "vite/README.md"
        Path("vite/README.md") → "vite/README.md"
        Path("./vite/README.md") → "vite/README.md"
    """
    try:
        # Resolve to absolute, then make relative to project root
        absolute_path = path.resolve()
        project_root = Path.cwd()
        return str(absolute_path.relative_to(project_root))
    except ValueError:
        # Path is outside project (edge case) - return as-is
        return str(path)


def _validate_url(url: str) -> None:
    """Validate URL has scheme and netloc, exit if invalid."""
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        print(f"❌ Error: INVALID_URL|{url}|")
        sys.exit(1)


def _validate_directory_for_collection(dir_path: Path, index_path: Path) -> None:
    """Validate directory is suitable for docs collection, exit if invalid."""
    if dir_path.exists() and not index_path.exists() and any(dir_path.iterdir()):
        print(
            f"❌ Error: INVALID_COLLECTION|"
            f"Directory non-empty and missing INDEX.xml. "
            f"Rejected to prevent inadvertent file overwrites|{dir_path}|"
        )
        sys.exit(1)


def _slugify_title(title: str) -> str:
    """Convert title to filename-safe slug."""
    slug = title.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[-\s]+", "-", slug)
    return slug.strip("-")


def _get_duplicate_title_count(dir_path: Path, title: str, source_url: str) -> int:
    """Count existing sources with same title but different URL.

    Returns:
        int: Number of existing sources with matching title and different URL
             (0 if no duplicates, used to calculate suffix)
    """
    index_path = dir_path / "INDEX.xml"

    # If INDEX doesn't exist yet, no duplicates possible
    if not index_path.exists():
        return 0

    # Parse INDEX.xml
    tree = ET.parse(index_path)
    root = tree.getroot()

    count = 0
    for source in root.findall("source"):
        title_elem = source.find("title")
        url_elem = source.find("source_url")

        # Count if same title AND different URL
        if (
            title_elem is not None
            and title_elem.text == title
            and url_elem is not None
            and url_elem.text != source_url
        ):
            count += 1

    return count


def _create_readme(dir_path: Path, source_site_url: str) -> None:
    """Create README.md for new collection with overview and source link."""
    readme_content = f"""# {dir_path.name} Documentation

Curated docs for targeted AI context.

- Curation Index: [INDEX.xml](INDEX.xml)
- Curation Source: <{source_site_url}>
"""
    readme_path = dir_path / "README.md"
    readme_path.write_text(readme_content)
    print(f"✅ Created curation readme|{_format_path_for_display(readme_path)}|")


def _create_index_xml(dir_path: Path) -> None:
    """Create empty INDEX.xml structure."""
    root = ET.Element("docs_index")
    ET.indent(root, space="  ")

    tree = ET.ElementTree(root)
    index_path = dir_path / "INDEX.xml"
    tree.write(index_path, encoding="unicode", xml_declaration=False)
    print(f"✅ Created curation index|{_format_path_for_display(index_path)}|")


def _add_or_update_source_in_index(
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

    if is_update:
        print(f"✅ Updated index source|{_format_path_for_display(index_path)}|")
    else:
        print(f"✅ Added index source|{_format_path_for_display(index_path)}|")

    print("💡 INDEX.xml <description> pending: PLACEHOLDER requires summary|")

    # Return Path object for cleanup (if filename changed)
    old_file_path = (
        (dir_path / old_filename) if old_filename and old_filename != local_file else None
    )
    return is_update, old_file_path


def _cleanup_old_file(old_file_path: Path | None) -> None:
    """Delete old markdown file if filename changed during update.

    Args:
        old_file_path: Path to previous file to remove (or None if no cleanup needed)
    """
    if old_file_path:
        old_file_path.unlink(missing_ok=True)
        print(f"🗑️ Removed old file|{_format_path_for_display(old_file_path)}|")


def _get_firecrawl_client() -> Firecrawl:
    """Get Firecrawl client with API key from environment."""
    api_key = environ.get("API_KEY_MCP_FIRECRAWL")
    if not api_key:
        print("❌ Error: MISSING_API_KEY|API_KEY_MCP_FIRECRAWL not set|")
        sys.exit(1)
    return Firecrawl(api_key=api_key)


def _parse_retry_seconds(error: RateLimitError) -> int:
    """Parse retry-after seconds from rate limit error message."""
    error_msg = str(error)
    retry_match = re.search(r"retry after (\d+)s", error_msg, re.IGNORECASE)
    if retry_match:
        return int(retry_match.group(1))
    # Default to 60s if pattern not found (rate limit window is per minute)
    return 60


def _extract_metadata(result: Document) -> dict:
    """Extract title from Firecrawl document metadata."""
    metadata = {}
    if hasattr(result, "metadata") and result.metadata:
        metadata = {
            "title": getattr(result.metadata, "title", "Untitled"),
        }
    return metadata


def _perform_scrape(firecrawl: Firecrawl, url: str) -> dict:
    """Perform single scrape attempt.

    Args:
        firecrawl: Configured Firecrawl client
        url: URL to scrape

    Returns:
        Dict with markdown content and metadata

    Raises:
        RateLimitError: If rate limited
        FirecrawlError: For other Firecrawl API errors
        SystemExit(1): If scrape returns no content (NO_CONTENT error)
    """
    result = firecrawl.scrape(
        url,
        formats=["markdown"],
        only_main_content=True,  # Excl. nav menu, footer, sidebars, etc.
        remove_base64_images=True,  # Removes base64 strings (keeps alt text)
        wait_for=3000,  # Wait to capture dynamic content (3 seconds)
        max_age=86400000,  # Use cached content for speed (24 hours)
    )

    # Validate result
    if not result or not hasattr(result, "markdown") or not result.markdown:
        print(f"❌ Error: NO_CONTENT|No scrape content returned|{url}|")
        sys.exit(1)

    return {
        "markdown": result.markdown,
        "metadata": _extract_metadata(result),
    }


def _scrape_with_firecrawl(url: str, max_attempts: int = 2) -> dict:
    """Scrape URL using Firecrawl Python SDK with automatic retry on rate limits.

    Automatically retries if rate limited, waiting the duration specified in the
    error message plus a 2-second safety buffer. Non-rate-limit errors exit immediately
    without retry.

    Args:
        url: URL to scrape
        max_attempts: Maximum total scrape attempts (default: 2 = initial + 1 retry)

    Returns:
        Dict with 'markdown' (str) and 'metadata' (dict) keys

    Raises:
        SystemExit(1): On rate limit, API, network, or unexpected errors
    """
    firecrawl = _get_firecrawl_client()

    # Attempt loop (zero-indexed: 0, 1, ... max_attempts-1)
    for attempt in range(max_attempts):
        try:
            return _perform_scrape(firecrawl, url)

        except RateLimitError as e:
            if attempt < max_attempts - 1:  # More attempts available
                retry_seconds = _parse_retry_seconds(e)
                wait_time = retry_seconds + 2  # Add 2s safety buffer
                print(f"⏳ Rate limited|Waiting {wait_time}s before retry...|")
                time.sleep(wait_time)
                continue

            # Final attempt exhausted
            print(
                f"❌ Error: FIRECRAWL_RATELIMIT|"
                f"Firecrawl rate limited all {max_attempts} attempts, "
                f"no content scraped|{url}|"
            )
            sys.exit(1)

        except FirecrawlError as e:
            # All other Firecrawl API errors
            print(f"❌ Error: FIRECRAWL|{e}|{url}|")
            sys.exit(1)

        except OSError as e:
            # Network/connection failures (timeouts, DNS errors, etc.)
            print(f"❌ Error: NETWORK|{e}|{url}|")
            sys.exit(1)

        except Exception as e:  # noqa: BLE001
            # Unexpected errors (ValueError, RuntimeError, SDK bugs, etc.)
            print(f"❌ Error: UNEXPECTED|{type(e).__name__}: {e}|{url}|")
            sys.exit(1)

    # Defensive fallback (unreachable in normal execution)
    print(f"❌ Error: NETWORK|Failed after {max_attempts} attempts|{url}|")
    sys.exit(1)


def main() -> None:
    """Add or update documentation in a collection directory.

    Workflow:
        1. Validate URL and directory
        2. Scrape content from URL (with rate limit retry)
        3. Create collection structure if new (README.md, INDEX.xml)
        4. Generate filename from title (with suffix for duplicates)
        5. Write markdown file and update INDEX.xml
        6. Clean up old file if filename changed
    """
    parser = argparse.ArgumentParser(
        description="Add or update documentation in a collection directory"
    )

    parser.add_argument("directory", help="Documentation directory (e.g. `tailwind/`)")
    parser.add_argument("source_url", help="Web URL to scrape and add new document from")

    args = parser.parse_args()

    source_url = args.source_url
    dir_path = _normalise_directory_path(args.directory)
    index_path = dir_path / "INDEX.xml"

    _validate_url(source_url)
    _validate_directory_for_collection(dir_path, index_path)

    # Print initial status message
    print(f"✅ Starting to curate from|{source_url}|")

    # Ensure directory exists
    dir_path.mkdir(parents=True, exist_ok=True)

    # Scrape with FireCrawl (do this before creating files to fail fast)
    scraped_doc = _scrape_with_firecrawl(source_url, max_attempts=2)
    content = scraped_doc["markdown"]
    metadata = scraped_doc["metadata"]

    # Confirm successful scrape
    char_count = len(content)
    print(f"✅ Scraped content|({char_count:,} characters)|")

    title = metadata.get("title", "Untitled")

    # Extract source site URL (scheme + netloc) for README collection source
    parsed_url = urlparse(source_url)
    source_site_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

    # Create README and INDEX if new collection
    if not index_path.exists():
        _create_readme(dir_path, source_site_url)
        _create_index_xml(dir_path)

    # Generate filename from title (with suffix if duplicate title exists)
    base_slug = _slugify_title(title)
    duplicate_count = _get_duplicate_title_count(dir_path, title, source_url)

    if duplicate_count == 0:
        filename = f"{base_slug}.md"
    else:
        filename = f"{base_slug}-{duplicate_count + 1}.md"

    file_path = dir_path / filename

    # Write markdown file (overwrites if exists)
    file_path.write_text(content)
    print(f"✅ Written scrape to file|{_format_path_for_display(file_path)}|")

    # Update INDEX.xml (add or update)
    is_update, old_file_path = _add_or_update_source_in_index(
        dir_path, title, source_url, filename
    )

    # Cleanup old .md file if filename changed
    _cleanup_old_file(old_file_path)

    # Print final success message
    if is_update:
        print("🎉 Curation Success!|scraped, overwrote and re-indexed document|\n")
    else:
        print("🎉 Curation Success!|scraped, added and indexed document|\n")


if __name__ == "__main__":
    main()
