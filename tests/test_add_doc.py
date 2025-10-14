"""Tests for add_doc.py script."""

import subprocess
import tempfile
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
            assert "not a valid URL" in output or "invalid URL" in output


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

            index_path = new_dir / "INDEX.xml"
            assert f"✅ Created empty INDEX.xml at {index_path}" in output
            assert index_path.exists()

            readme_path = new_dir / "README.md"
            assert f"✅ Successfully added {readme_path}" in output
            assert readme_path.exists()

            # Check that a markdown file was created (dynamic filename from real scrape)
            md_files = [
                f
                for f in new_dir.iterdir()
                if f.suffix == ".md" and f.name != "README.md"
            ]
            assert len(md_files) == 1
            assert md_files[0].name in output

            assert "✅ Added new <source> to INDEX.xml with local_file:" in output
            assert f"✅ Successfully added and indexed: {md_files[0].name}" in output

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
            assert f"✅ Successfully added {readme_path}" in output
            assert readme_path.exists()

            index_path = empty_dir / "INDEX.xml"
            assert f"✅ Created empty INDEX.xml at {index_path}" in output
            assert index_path.exists()

            # Check that a markdown file was created (dynamic filename from real scrape)
            md_files = [
                f
                for f in empty_dir.iterdir()
                if f.suffix == ".md" and f.name != "README.md"
            ]
            assert len(md_files) == 1

            assert "✅ Added new <source> to INDEX.xml with local_file:" in output
            assert f"✅ Successfully added and indexed: {md_files[0].name}" in output

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

            assert "✅ Added new <source> to INDEX.xml with local_file:" in output
            assert f"✅ Successfully added and indexed: {md_files[0].name}" in output

            # README should NOT be created
            readme_path = existing_dir / "README.md"
            assert not readme_path.exists()
            assert f"✅ Successfully added {readme_path}" not in output

    def test_nonempty_noncollection_directory_fails(self) -> None:
        """Nonempty directory without INDEX.xml fails with clear error message."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            non_collection_dir = tmp_path / "not_a_collection"

            non_collection_dir.mkdir()
            (non_collection_dir / "some_file.txt").write_text("random content")

            exit_code, output = run_script(str(non_collection_dir), TEST_URL)

            # Assert failure
            assert exit_code != 0

            expected_msg = (
                f"Error: ❌ Directory '{non_collection_dir}' is not empty and "
                f"missing INDEX.xml. Use an empty directory or a valid docs collection."
            )
            assert expected_msg in output

    def test_duplicate_url_updates_source(self) -> None:
        """Adding same URL twice should update existing source, not fail."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            collection_dir = tmp_path / "test_collection"

            # First add - should succeed
            exit_code1, output1 = run_script(str(collection_dir), TEST_URL)
            assert exit_code1 == 0
            assert "✅ Added new <source> to INDEX.xml" in output1
            assert "✅ Successfully added and indexed:" in output1

            # Second add with same URL - should UPDATE (not fail)
            exit_code2, output2 = run_script(str(collection_dir), TEST_URL)
            assert exit_code2 == 0  # Should succeed
            assert "💡 Updating existing source for:" in output2
            assert "♻️ Re-scraped and updated:" in output2

            # Verify INDEX.xml has only ONE source entry (not two)
            index_path = collection_dir / "INDEX.xml"
            index_content = index_path.read_text()
            source_count = index_content.count("<source>")
            assert source_count == 1, f"Expected 1 source, found {source_count}"


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

            # Assert XML structure
            assert "<docs_index>" in index_content
            assert "</docs_index>" in index_content
            assert "<source>" in index_content
            assert "</source>" in index_content
            assert "<title>" in index_content
            assert "</title>" in index_content
            assert "<local_file>" in index_content
            assert "</local_file>" in index_content

            # Assert fields we have so far
            assert "<description>PLACEHOLDER</description>" in index_content
            assert f"<source_url>{TEST_URL}</source_url>" in index_content

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
            assert "Curated docs for targeted AI context." in readme_content
            assert "[INDEX.xml](INDEX.xml)" in readme_content
            assert "https://zustand.docs.pmnd.rs" in readme_content
