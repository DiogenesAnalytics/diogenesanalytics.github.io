"""Tests for website."""

import filecmp
import os
import shutil
from pathlib import Path
from typing import List
from typing import Set
from typing import Tuple

import pytest


def get_project_directory() -> Path:
    """Get project directory path object."""
    # get the path of the current file (test_file.py)
    current_file_path = Path(os.path.abspath(__file__))

    # get grand parent dir
    return current_file_path.parents[1]


def clone_directory(src: Path, dst: Path) -> None:
    """Clone a directory recursively to another location."""
    # ensure the destination directory exists
    if not dst.exists():
        dst.mkdir(parents=True)

    # copy everything in the source directory to the destination
    shutil.copytree(src, dst, dirs_exist_ok=True)


def compare_directories(
    src: Path, dst: Path, ignore_dirs: Set[str]
) -> List[Tuple[Path, Path]]:
    """Recursively compare two directories and return differences."""
    differences = []

    # Compare files in the current directory
    comparison = filecmp.dircmp(src, dst)

    # Check for differing files
    for file in comparison.diff_files:
        differences.append((src / file, dst / file))

    # Check for files only in src (i.e., missing in dst)
    for file in comparison.left_only:
        differences.append((src / file, dst / file))

    # Check for files only in dst (i.e., extra in dst)
    for file in comparison.right_only:
        differences.append((src / file, dst / file))

    # Check subdirectories
    for subdir_name, subdir_cmp in comparison.subdirs.items():
        if subdir_name not in ignore_dirs:
            subdir_differences = compare_directories(
                Path(subdir_cmp.left), Path(subdir_cmp.right), ignore_dirs
            )
            if subdir_differences:  # If subdir contains differences, add it
                differences.append(
                    (Path(subdir_cmp.left), Path(subdir_cmp.right))
                )
                differences.extend(subdir_differences)

    return differences


@pytest.fixture(scope="function")
def project_dir() -> Path:
    """Get the path of the project directory."""
    return get_project_directory()


@pytest.fixture(scope="function")
def ignore_dirs() -> Set[str]:
    """Create set of all dirs to ignore."""
    return {".github", ".jekyll-cache", ".mypy_cache", ".pytest_cache"}


@pytest.fixture(scope="function")
def temp_project_dir(tmp_path: Path, project_dir: Path) -> Path:
    """Create a temporary directory to copy the source files for testing."""
    # create new temp web src dir
    tmp_src = tmp_path / "web_src"
    tmp_src.mkdir(parents=True)

    # now clone
    clone_directory(project_dir, tmp_src)

    # get tmp src path
    return tmp_src


@pytest.fixture(scope="function")
def comp_dirs_test_data(tmp_path: Path) -> Tuple[Path, Path]:
    """Create temporary directories for testing and return source and destination."""
    # create a source directory
    src = tmp_path / "source"
    src.mkdir()

    # create some files in the source directory
    (src / "file1.txt").write_text("file1 content")
    (src / "file2.txt").write_text("file2 content")
    (src / "subdir").mkdir()
    (src / "subdir" / "file3.txt").write_text("file3 content")

    # create a destination directory, and copy contents from the source
    dst = tmp_path / "destination"
    shutil.copytree(src, dst)

    # modify a file in the destination to create a difference
    (dst / "file2.txt").write_text("modified file2 content")

    # delete a file in the destination to create a difference
    (dst / "subdir" / "file3.txt").unlink()

    # create an extra file in the destination
    (dst / "file4.txt").write_text("extra file in destination")

    return src, dst


@pytest.mark.utils
def test_compare_directories(
    comp_dirs_test_data: Tuple[Path, Path], ignore_dirs: Set[str]
) -> None:
    """Test compare_directories for detecting differences."""
    # unpack dirs
    src, dst = comp_dirs_test_data

    # Sort differences to ensure consistent order
    differences = sorted(compare_directories(src, dst, ignore_dirs))

    # Sort expected differences the same way
    expected_differences = sorted(
        [
            (src / "file2.txt", dst / "file2.txt"),
            (src / "subdir" / "file3.txt", dst / "subdir" / "file3.txt"),
            (src / "file4.txt", dst / "file4.txt"),
            (src / "subdir", dst / "subdir"),
        ]
    )

    # check if sorted differences match
    assert len(differences) == len(expected_differences), (
        f"Expected {len(expected_differences)} differences, but got "
        f"{len(differences)}. Differences: {differences}"
    )

    # check each
    for expected, actual in zip(expected_differences, differences, strict=True):
        assert expected == actual, f"Expected {expected} but got {actual}"


@pytest.mark.fixture
def test_clone_directory(
    temp_project_dir: Path, project_dir: Path, ignore_dirs: Set[str]
) -> None:
    """Test if the project source directory is cloned correctly."""
    # collect all differences between the project directory and temp directory
    differences = compare_directories(
        project_dir, temp_project_dir, ignore_dirs
    )

    # no differences
    assert not differences, f"Differences found: {differences}"
