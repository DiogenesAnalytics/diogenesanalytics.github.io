"""Tests for Makefile."""

import subprocess
from typing import List
from typing import Optional

from pytest import MonkeyPatch


def run_make(
    target: str, dry_mode: bool = False, extra_args: Optional[List[str]] = None
) -> subprocess.CompletedProcess:
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
        command: List[str], *args, **kwargs
    ) -> subprocess.CompletedProcess:
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
        command: List[str], *args, **kwargs
    ) -> subprocess.CompletedProcess:
        """Mock function for subprocess.run to simulate command execution."""
        # check that the extra arguments are in the command list
        assert "--jobs" in command
        assert "4" in command
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    # replace subprocess.run with our mock function during the test
    monkeypatch.setattr(subprocess, "run", mock_subprocess_run)

    # call run_make with extra_args set to ['--jobs', '4']
    run_make("build", extra_args=["--jobs", "4"])
