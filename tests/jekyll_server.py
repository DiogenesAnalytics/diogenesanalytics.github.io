"""Tools for running Jekyll."""

import subprocess
from pathlib import Path
from typing import Optional
from typing import Union


class JekyllServer:
    """Manages a Jekyll server instance using subprocess."""

    def __init__(
        self,
        cwd: Union[Path, str],
        host: str = "127.0.0.1",
        port: int = 4000,
        source: Optional[str] = None,
    ) -> None:
        """Setup Jekyll server."""
        self.cwd = Path(cwd)
        self.host = host
        self.port = port
        self.source = source
        self.process: Optional[subprocess.Popen[str]] = None

    def start(self) -> None:
        """Start the Jekyll server."""
        # check if current process running
        if self.process is not None:
            print(
                "Warning: Jekyll server is already running. "
                "Use `stop()` to stop the server before starting a new one."
            )

        # start new process
        else:
            # build command
            command = [
                "jekyll",
                "serve",
                "--host",
                self.host,
                "--port",
                str(self.port),
            ]

            # check optional src arg
            if self.source:
                command.extend(["--source", self.source])

            # start proc
            self.process = subprocess.Popen(
                command,
                cwd=self.cwd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            # notify
            print(
                f"Jekyll server started on "
                f"{self.host}:{self.port} with source={self.source}."
            )

    def stop(self) -> None:
        """Stop the Jekyll server."""
        if self.process:
            # graceful shutdown
            self.process.terminate()

            try:
                # wait for termination
                self.process.wait(timeout=1)
            except subprocess.TimeoutExpired:
                # force kill if it times out
                self.process.kill()

            # notify
            print("Jekyll server stopped.")


def run_jekyll_build(
    site_dir: Path, destination: Optional[Path] = None
) -> subprocess.CompletedProcess[str]:
    """Runs `jekyll build` in the specified directory."""
    # build cmd
    cmd = ["jekyll", "build", "--source", str(site_dir)]

    # add optional destination
    if destination:
        cmd += ["--destination", str(destination)]

    # start process
    return subprocess.run(
        cmd,
        cwd=site_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
