"""Tests for website."""

import filecmp
import os
import shutil
import subprocess
import time
from pathlib import Path
from typing import Generator
from typing import List
from typing import Set
from typing import Tuple

import pytest
import requests
from pytest import TempPathFactory
from seleniumbase import BaseCase

from tests.jekyll_server import JekyllServer
from tests.jekyll_server import SimpleHTTPServer
from tests.jekyll_server import run_jekyll_build


def get_project_directory() -> Path:
    """Get project directory path object."""
    # get the path of the current file (test_file.py)
    current_file_path = Path(os.path.abspath(__file__))

    # get grand parent dir
    return current_file_path.parents[1]


def clone_directory(src: Path, dst: Path, ignore_dirs: Set[str]) -> None:
    """Clone a directory recursively to another location."""
    # ensure the destination directory exists
    if not dst.exists():
        dst.mkdir(parents=True)

    # copy everything in the source directory to the destination
    shutil.copytree(
        src,
        dst,
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns(*ignore_dirs),
    )


def compare_directories(
    src: Path, dst: Path, ignore_dirs: Set[str]
) -> List[Tuple[Path, Path]]:
    """Recursively compare two dirs and return diff while ignoring key dirs."""
    # container for any diffs found
    differences = []

    # compare files in the current directory
    comparison = filecmp.dircmp(src, dst)

    # ignore the specified directories at the root level
    left_only_filtered = [
        f for f in comparison.left_only if f not in ignore_dirs
    ]
    right_only_filtered = [
        f for f in comparison.right_only if f not in ignore_dirs
    ]

    # check for differing files
    for file in comparison.diff_files:
        differences.append((src / file, dst / file))

    # check for files only in src (i.e., missing in dst)
    for file in left_only_filtered:
        differences.append((src / file, dst / file))

    # check for files only in dst (i.e., extra in dst)
    for file in right_only_filtered:
        differences.append((src / file, dst / file))

    # check subdirectories
    for subdir_name, subdir_cmp in comparison.subdirs.items():
        # ignore subdirs if in ignored dirs
        if subdir_name not in ignore_dirs:
            # get diffs again
            subdir_differences = compare_directories(
                Path(subdir_cmp.left), Path(subdir_cmp.right), ignore_dirs
            )

            # diffs found ...
            if subdir_differences:
                # add to dirs with diffs
                differences.append(
                    (Path(subdir_cmp.left), Path(subdir_cmp.right))
                )

                # then add their content's diffs
                differences.extend(subdir_differences)

    return differences


@pytest.fixture(scope="session")
def project_dir() -> Path:
    """Get the path of the project directory."""
    return get_project_directory()


@pytest.fixture(scope="session")
def ignore_dirs() -> Set[str]:
    """Create set of all dirs to ignore."""
    return {
        "_site",
        ".git",
        ".github",
        ".jekyll-cache",
        ".mypy_cache",
        ".pytest_cache",
    }


@pytest.fixture(scope="function")
def temp_project_dir(
    tmp_path: Path, project_dir: Path, ignore_dirs: Set[str]
) -> Path:
    """Create a temporary directory to copy the source files for testing."""
    # create new temp web src dir
    tmp_src = tmp_path / "web_src_function"
    tmp_src.mkdir(parents=True)

    # now clone
    clone_directory(project_dir, tmp_src, ignore_dirs)

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


@pytest.fixture(scope="function")
def jekyll_server(
    temp_project_dir: Path,
) -> Generator[JekyllServer, None, None]:
    """Fixture to create a JekyllServer instance, with auto cleanup after the test."""
    # get instance
    server = JekyllServer(cwd=temp_project_dir)

    # start the server before the test
    server.start()

    # yield the server instance to the test
    yield server

    # cleanup (stop the server) after the test
    server.stop()


@pytest.fixture(scope="session")
def built_site(
    tmp_path_factory: TempPathFactory, project_dir: Path, ignore_dirs: Set[str]
) -> Path:
    """Clone project dir, build Jekyll site, reuse it for all tests."""
    # Create a temp directory for the Jekyll project
    temp_project_dir = tmp_path_factory.mktemp("web_src_session")

    # Clone the project files into the temp directory
    clone_directory(project_dir, temp_project_dir, ignore_dirs)

    # Run Jekyll build once
    run_jekyll_build(temp_project_dir)

    # Return the _site directory for serving
    return temp_project_dir / "_site"


@pytest.fixture(scope="session")
def static_site_server(
    built_site: Path,
) -> Generator[SimpleHTTPServer, None, None]:
    """Serve the pre-built Jekyll site using a simple HTTP server."""
    # start server
    server = SimpleHTTPServer(built_site)
    server.start()

    # generate
    yield server

    # cleanup
    server.stop()


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

    # no differences should be found in the tracked files
    assert not differences, f"Differences found: {differences}"

    # ensure ignored directories are indeed missing in the cloned directory
    for ignored in ignore_dirs:
        assert not (
            temp_project_dir / ignored
        ).exists(), f"Ignored directory {ignored} was copied!"


@pytest.mark.jekyll
def test_jekyll_installed() -> None:
    """Test that Jekyll is installed and accessible."""
    try:
        # run the `jekyll --version` command to check if Jekyll is installed
        result = subprocess.run(
            ["jekyll", "--version"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        # check the return code, it should be 0 if successful
        assert (
            result.returncode == 0
        ), f"Jekyll command failed with return code {result.returncode}"

        # check if Jekyll is in the version output
        assert (
            "jekyll" in result.stdout.lower()
        ), "Jekyll is not installed or accessible"

    except subprocess.CalledProcessError as e:
        pytest.fail(f"Jekyll is not installed or not accessible: {e.stderr}")


@pytest.mark.jekyll
def test_jekyll_server_start_stop(jekyll_server: JekyllServer) -> None:
    """Test that the Jekyll server starts and stops correctly."""
    # Check that the process is running initially
    assert jekyll_server.process is not None
    assert jekyll_server.process.poll() is None

    # sleep
    time.sleep(0.1)

    # Check that the server process is terminated
    assert jekyll_server.process.poll() is None


@pytest.mark.jekyll
def test_jekyll_server_explicit_stop(jekyll_server: JekyllServer) -> None:
    """Test the explicit stop method of the Jekyll server."""
    # start the server
    jekyll_server.start()

    # check process running
    assert jekyll_server.process is not None
    assert jekyll_server.process.poll() is None

    # explicitly stop the server
    jekyll_server.stop()

    # check that the server process is terminated
    assert jekyll_server.process.poll() is not None


@pytest.mark.jekyll
def test_jekyll_server_initialize(
    temp_project_dir: Path, jekyll_server: JekyllServer
) -> None:
    """Test the initialization of the JekyllServer class."""
    assert jekyll_server.cwd == temp_project_dir
    assert jekyll_server.host == "127.0.0.1"
    assert jekyll_server.port == 4000
    assert jekyll_server.source is None
    assert jekyll_server.process is not None


@pytest.mark.jekyll
def test_jekyll_build(temp_project_dir: Path) -> None:
    """Test that `jekyll build` runs successfully and `_site` directory is created."""
    # run the Jekyll build function
    result = run_jekyll_build(temp_project_dir)

    # ensure the build command executed successfully
    assert result.returncode == 0, f"Jekyll build failed: {result.stderr}"

    # verify that `_site` directory was created
    _site_dir = temp_project_dir / "_site"
    assert (
        _site_dir.exists() and _site_dir.is_dir()
    ), "_site directory was not created!"


@pytest.mark.website
def test_website_is_up(static_site_server: SimpleHTTPServer) -> None:
    """Simple test to check if the website is up and accessible."""
    try:
        # send a GET request to the site
        response = requests.get(static_site_server.url())

        # confirm success
        assert response.status_code == 200

    # unaccessible
    except requests.exceptions.ConnectionError:
        pytest.fail("Failed to connect to Jekyll site.")


@pytest.mark.website
def test_homepage_title(
    sb: BaseCase, static_site_server: SimpleHTTPServer
) -> None:
    """Basic test to check if the homepage displays."""
    # load page into browser
    sb.open(static_site_server.url())

    # get title
    title = sb.get_title()
    assert (
        "error" not in title.lower()
    ), f"Page load error detected with title: {title}"
