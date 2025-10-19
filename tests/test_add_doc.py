"""Tests for add_doc.py script."""

import subprocess
import tempfile
from datetime import date
from pathlib import Path

# Test URL constant - valid documentation page for integration tests
TEST_URL = "https://zustand.docs.pmnd.rs/guides/updating-state"


def run_script(*args: str, cwd: Path | None = None) -> tuple[int, str]:
    """Run add_doc.py script via uv and return (exit_code, output)."""
    cmd = ["uv", "run", "python", "scripts/add_doc.py"]
    cmd.extend(args)

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=cwd,
        check=False,
    )

    return result.returncode, result.stdout + result.stderr


class TestInputValidation:
    """Fast tests for argument and URL validation (no API calls)."""

    def test_requires_both_directory_and_url_arguments(self) -> None:
        """Test that script requires both directory and url arguments."""
        # Test with no args
        exit_code, output = run_script()
        assert exit_code == 2
        assert "required" in output

    def test_fails_when_url_is_invalid(self) -> None:
        """Test that script exits with error when URL is invalid."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            exit_code, output = run_script(tmp_dir, "not-a-url")

            assert exit_code != 0
            assert "❌ Error: INVALID_URL|" in output


class TestDirectoryScenarios:
    """Integration tests for different directory states (requires API)."""

    def test_nonexistent_directory_creates_new_collection(self) -> None:
        """Nonexistent directory is created with README, INDEX.xml, scraped document."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            new_dir = tmp_path / "new_collection"

            exit_code, output = run_script(str(new_dir), TEST_URL)

            # Assert success and file paths in output
            assert exit_code == 0

            readme_path = new_dir / "README.md"
            index_path = new_dir / "INDEX.xml"

            # Assert creation messages appear in output
            assert f"✅ Created {readme_path}" in output
            assert f"✅ Created {index_path}" in output
            assert readme_path.exists()
            assert index_path.exists()

            # Check that a markdown file was created (dynamic filename from real scrape)
            md_files = [
                f
                for f in new_dir.iterdir()
                if f.suffix == ".md" and f.name != "README.md"
            ]
            assert len(md_files) == 1
            assert md_files[0].name in output

            assert "✅ Indexed in INDEX.xml:" in output
            # Full format validation: prefix|action|filepath|URL|
            # Script outputs absolute path for files outside project root
            assert (
                f"🎉 Curation Success!|"
                f"added and indexed document|"
                f"{md_files[0]}|"
                f"{TEST_URL}|"
            ) in output

    def test_empty_directory_creates_new_collection(self) -> None:
        """Empty directory is initialized with README, INDEX.xml, and scraped document."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            empty_dir = tmp_path / "empty_collection"

            empty_dir.mkdir()

            exit_code, output = run_script(str(empty_dir), TEST_URL)

            # Assert success and file paths in output
            assert exit_code == 0

            readme_path = empty_dir / "README.md"
            index_path = empty_dir / "INDEX.xml"

            # Script outputs absolute paths for files outside project root
            assert f"✅ Created {readme_path}" in output
            assert f"✅ Created {index_path}" in output
            assert readme_path.exists()
            assert index_path.exists()

            # Check that a markdown file was created (dynamic filename from real scrape)
            md_files = [
                f
                for f in empty_dir.iterdir()
                if f.suffix == ".md" and f.name != "README.md"
            ]
            assert len(md_files) == 1

            assert "✅ Indexed in INDEX.xml:" in output
            # Pattern matching only - simpler and less brittle
            assert "🎉 Curation Success!|added and indexed document|" in output

    def test_existing_collection_appends_without_readme(self) -> None:
        """Existing collection with INDEX.xml appends new doc without creating README."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            existing_dir = tmp_path / "existing_collection"

            existing_dir.mkdir()
            index_path = existing_dir / "INDEX.xml"
            index_path.write_text("<docs_index>\n</docs_index>\n")
            (existing_dir / "existing_file.md").write_text("# Existing content")

            exit_code, output = run_script(str(existing_dir), TEST_URL)

            # Assert success - only source added to INDEX.xml (no README created)
            assert exit_code == 0

            # Check that a markdown file was created (dynamic filename from real scrape)
            md_files = [
                f
                for f in existing_dir.iterdir()
                if f.suffix == ".md" and f.name not in ["README.md", "existing_file.md"]
            ]
            assert len(md_files) == 1

            assert "✅ Indexed in INDEX.xml:" in output
            # Pattern matching only
            assert "🎉 Curation Success!|added and indexed document|" in output

            # README should NOT be created
            readme_path = existing_dir / "README.md"
            assert not readme_path.exists()
            # Check that README creation message is not in output
            readme_created_count = output.count("README.md")
            assert readme_created_count == 0

    def test_nonempty_noncollection_directory_fails(self) -> None:
        """Nonempty directory without INDEX.xml fails with clear error message."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            invalid_dir = tmp_path / "not_a_collection"

            invalid_dir.mkdir()
            (invalid_dir / "some_file.txt").write_text("random content")

            exit_code, output = run_script(str(invalid_dir), TEST_URL)

            # Assert failure
            assert exit_code != 0
            assert (
                "❌ Error: INVALID_COLLECTION|"
                "Directory non-empty and missing INDEX.xml. "
                "Rejected to prevent inadvertent file overwrites|"
            ) in output

    def test_duplicate_url_updates_source(self) -> None:
        """Adding same URL twice should update existing source, not fail."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            collection_dir = tmp_path / "test_collection"

            # First add - should succeed
            exit_code1, output1 = run_script(str(collection_dir), TEST_URL)
            assert exit_code1 == 0
            assert "✅ Indexed in INDEX.xml:" in output1
            # Pattern matching only - first scrape (add)
            assert "🎉 Curation Success!|added and indexed document|" in output1

            # Second add with same URL - should UPDATE (not fail)
            exit_code2, output2 = run_script(str(collection_dir), TEST_URL)
            assert exit_code2 == 0  # Should succeed
            assert "✅ Updated in INDEX.xml:" in output2
            # Pattern matching only - second scrape (update)
            assert "🎉 Curation Success!|overwrote and re-indexed document|" in output2

            # Verify INDEX.xml has only ONE source entry (not two)
            index_path = collection_dir / "INDEX.xml"
            index_content = index_path.read_text()
            source_count = index_content.count("<source>")
            assert source_count == 1, f"Expected 1 source, found {source_count}"

    def test_duplicate_title_gets_unique_filename(self) -> None:
        """Two URLs with same title should create files with -2 suffix on second."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            collection_dir = tmp_path / "test_shiny"

            # First URL (Express API)
            run_script(str(collection_dir), "https://shiny.posit.co/py/api/express/")

            # Second URL (Testing API) - same title, different content
            run_script(str(collection_dir), "https://shiny.posit.co/py/api/testing/")

            # Both files should exist with unique names
            assert (collection_dir / "index-shiny-for-python.md").exists()
            assert (collection_dir / "index-shiny-for-python-2.md").exists()

            # Each file should contain different content
            file1_content = (collection_dir / "index-shiny-for-python.md").read_text()
            file2_content = (collection_dir / "index-shiny-for-python-2.md").read_text()
            assert "Express" in file1_content
            assert "Testing" in file2_content

            # INDEX.xml should have both entries with correct local_file values
            index_path = collection_dir / "INDEX.xml"
            index_content = index_path.read_text()
            assert "<local_file>index-shiny-for-python.md</local_file>" in index_content
            assert "<local_file>index-shiny-for-python-2.md</local_file>" in index_content


class TestOutputContent:
    """Integration tests validating generated file content (requires API)."""

    def test_index_xml_structure_and_content(self) -> None:
        """Test INDEX.xml has correct XML structure and content."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            new_dir = tmp_path / "test_collection"

            exit_code, _ = run_script(str(new_dir), TEST_URL)

            assert exit_code == 0

            index_path = new_dir / "INDEX.xml"
            index_content = index_path.read_text()

            # Assert XML structure and content based on TEST_URL
            today = date.today().isoformat()

            assert index_content.startswith("<docs_index>")
            assert "<source>\n" in index_content
            assert "<title>Updating state - Zustand</title>\n" in index_content
            assert "<description>PLACEHOLDER</description>\n" in index_content
            assert f"<source_url>{TEST_URL}</source_url>\n" in index_content
            assert "<local_file>updating-state-zustand.md</local_file>\n" in index_content
            assert f"<scraped_at>{today}</scraped_at>\n" in index_content
            assert "</source>\n" in index_content
            assert index_content.endswith("</docs_index>")

    def test_readme_md_contains_required_content(self) -> None:
        """Test README.md contains required content elements."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            new_dir = tmp_path / "test_collection"

            exit_code, _ = run_script(str(new_dir), TEST_URL)

            assert exit_code == 0

            readme_path = new_dir / "README.md"
            readme_content = readme_path.read_text()

            # Assert required content
            assert "# test_collection Documentation" in readme_content
            assert "Curated docs for targeted AI context.\n" in readme_content
            assert "- Curation Index: [INDEX.xml](INDEX.xml)\n" in readme_content
            assert "- Curation Source: <https://zustand.docs.pmnd.rs>\n" in readme_content
