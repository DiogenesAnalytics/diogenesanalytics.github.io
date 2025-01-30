"""Tests for Makefile."""

import subprocess
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple

import pytest
from pytest import MonkeyPatch


def run_make(
    target: str, dry_mode: bool = False, extra_args: Optional[List[str]] = None
) -> subprocess.CompletedProcess[str]:
    """Runs a Makefile target."""
    # initial command string
    command = ["make"]

    # check for -n flag
    if dry_mode:
        command.append("-n")

    # add in target command
    command.append(target)

    # add any additional args
    if extra_args:
        command.extend(extra_args)

    # run process and get output
    result = subprocess.run(command, capture_output=True, text=True)

    # done
    return result


@pytest.fixture(scope="function")
def print_config_output() -> Dict[str, str]:
    """Fixture to get the output from the print-config target in Makefile."""
    result = run_make("print-config")

    # ensure the command ran successfully
    assert result.returncode == 0

    # parse the output from print-config and store as key-value pairs
    config_data = {}
    for line in result.stdout.splitlines():
        # only process lines with a key-value format (e.g., key: value)
        if ":" in line:
            key, value = line.split(":", 1)
            config_data[key.strip()] = value.strip()

    return config_data


def test_no_empty_config_values(print_config_output: Dict[str, str]) -> None:
    """Test that none of the values in the print-config output are empty."""
    for value in print_config_output.values():
        assert (
            value != ""
        ), f"One of the config values is empty! Output:\n {print_config_output}"


def test_github_info_matches_docker_images(
    print_config_output: Dict[str, str]
) -> None:
    """Test that GitHub user, repo name, and branch match the Docker images."""
    # extract values
    github_user = print_config_output["GitHub User"]
    repo_name = print_config_output["Repository Name"]
    git_branch = print_config_output["Git Branch"]

    # rebuild the expected Docker image names
    expected_jupyter_image = (
        f"ghcr.io/{github_user}/{repo_name}:{git_branch}_jupyter"
    )
    expected_testing_image = (
        f"ghcr.io/{github_user}/{repo_name}:{git_branch}_testing"
    )

    # extract the actual Docker images
    jupyter_image = print_config_output["Docker Jupyter Image"]
    testing_image = print_config_output["Docker Testing Image"]

    # assert that the rebuilt Docker images match the ones in the output
    assert expected_jupyter_image == jupyter_image
    assert expected_testing_image == testing_image


def test_github_user_extraction_https() -> None:
    """Test GitHub username extraction from HTTPS URL."""
    # setup url
    remote_url = "https://github.com/User_Name/repo_name.git"
    result = run_make(
        "test-github-user", extra_args=[f"REMOTE_URL={remote_url}"]
    )

    # check exit value
    assert result.returncode == 0

    # cleanup output
    output = result.stdout.strip()

    # check user name
    assert output == "user_name"


def test_github_user_extraction_ssh() -> None:
    """Test GitHub username extraction from SSH URL."""
    # setup url
    remote_url = "git@github.com:User_Name/repo_name.git"
    result = run_make(
        "test-github-user", extra_args=[f"REMOTE_URL={remote_url}"]
    )

    # check exit value
    assert result.returncode == 0

    # cleaup output
    output = result.stdout.strip()

    # check user name
    assert output == "user_name"


def test_run_make_invalid_target() -> None:
    """Confirm missing target fails."""
    # run make on missing target
    result = run_make("nonexistent_target", dry_mode=True)

    # check correct error
    assert result.returncode != 0
    assert "No rule to make target" in result.stderr


def test_run_make_dry_mode(monkeypatch: MonkeyPatch) -> None:
    """Test the behavior of `run_make` with dry-run mode enabled."""

    def mock_subprocess_run(
        command: List[str], *args: Tuple[Any], **kwargs: Dict[str, Any]
    ) -> subprocess.CompletedProcess[str]:
        """Mock function for subprocess.run to simulate command execution."""
        # check that "-n" (dry-run flag) is in the command list
        assert "-n" in command

        # check that the target name "build" is in the command list
        assert "build" in command

        # simulate a successful subprocess result
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    # replace subprocess.run with our mock function during the test
    monkeypatch.setattr(subprocess, "run", mock_subprocess_run)

    # call run_make with dry_mode set to True
    run_make("build", dry_mode=True)


def test_run_make_with_extra_args(monkeypatch: MonkeyPatch) -> None:
    """Test the `run_make` function with additional arguments."""

    def mock_subprocess_run(
        command: List[str], *args: Tuple[Any], **kwargs: Dict[str, Any]
    ) -> subprocess.CompletedProcess[str]:
        """Mock function for subprocess.run to simulate command execution."""
        # check that the extra arguments are in the command list
        assert "--jobs" in command
        assert "4" in command
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    # replace subprocess.run with our mock function during the test
    monkeypatch.setattr(subprocess, "run", mock_subprocess_run)

    # call run_make with extra_args set to ['--jobs', '4']
    run_make("build", extra_args=["--jobs", "4"])


def test_check_docker_dry_run() -> None:
    """Test `check-docker` make target executes the expected command."""
    result = run_make("check-docker", dry_mode=True)

    # verify that the expected command appears in the dry run output
    assert "docker --version" in result.stdout
    assert result.returncode == 0


def test_check_deps_tests_without_notty_defined() -> None:
    """Test that NOTTY is correctly handled when not set."""
    result = run_make("check-deps-tests", dry_mode=True)
    assert result.returncode == 0
    assert "-it" in result.stdout  # Ensure -it is included


def test_check_deps_tests_with_notty() -> None:
    """Test that NOTTY is correctly handled in check-deps-tests."""
    result = run_make(
        "check-deps-tests", extra_args=["NOTTY=true"], dry_mode=True
    )
    assert result.returncode == 0
    assert "-i" in result.stdout
    assert "-it" not in result.stdout  # Ensure -it is not included


def test_check_deps_tests_without_notty() -> None:
    """Test that NOTTY is correctly handled when false."""
    result = run_make(
        "check-deps-tests", extra_args=["NOTTY=false"], dry_mode=True
    )
    assert result.returncode == 0
    assert "-it" in result.stdout  # Ensure -it is included


def test_build_jupyter_no_options() -> None:
    """Test build-jupyter target without DCKR_PULL or DCKR_NOCACHE options."""
    result = run_make("build-jupyter", dry_mode=True)

    # Check that docker pull/build is in command, but no --no-cache flag
    assert "docker pull" in result.stdout
    assert "docker build" in result.stdout
    assert "--no-cache" not in result.stdout


def test_build_jupyter_with_nocache() -> None:
    """Test the build-jupyter target with DCKR_NOCACHE option."""
    result = run_make(
        "build-jupyter", dry_mode=True, extra_args=["DCKR_NOCACHE=true"]
    )

    # Check that --no-cache flag is passed to docker build
    assert "docker build" in result.stdout
    assert "--no-cache" in result.stdout
    assert "docker pull" in result.stdout


def test_build_jupyter_with_no_pull() -> None:
    """Test build-jupyter target with no DCKR_PULL."""
    result = run_make(
        "build-jupyter", dry_mode=True, extra_args=["DCKR_PULL=false"]
    )

    # check that docker pull not included in the output
    assert "docker pull" not in result.stdout
    assert "docker build" in result.stdout
    assert "--no-cache" not in result.stdout


def test_build_tests_no_options() -> None:
    """Test build-tests target without DCKR_PULL or DCKR_NOCACHE options."""
    result = run_make("build-tests", dry_mode=True)

    # Check that docker pull/build is in command, but no --no-cache flag
    assert "docker pull" in result.stdout
    assert "docker build" in result.stdout
    assert "--no-cache" not in result.stdout


def test_build_tests_with_nocache() -> None:
    """Test the build-tests target with DCKR_NOCACHE option."""
    result = run_make(
        "build-tests", dry_mode=True, extra_args=["DCKR_NOCACHE=true"]
    )

    # Check that --no-cache flag is passed to docker build
    assert "docker build" in result.stdout
    assert "--no-cache" in result.stdout
    assert "docker pull" in result.stdout


def test_build_tests_with_no_pull() -> None:
    """Test build-tests target with no DCKR_PULL."""
    result = run_make(
        "build-tests", dry_mode=True, extra_args=["DCKR_PULL=false"]
    )

    # check that docker pull not included in the output
    assert "docker pull" not in result.stdout
    assert "docker build" in result.stdout
    assert "--no-cache" not in result.stdout
