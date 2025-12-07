#!/usr/bin/env python3
"""CLI tool for filtering Jupyter notebooks by front-matter metadata."""

import sys
from pathlib import Path

import click
from filter_notebook.filter import should_publish


@click.command()
@click.argument("notebook", type=str)
@click.option(
    "--input-dir",
    "-i",
    type=click.Path(file_okay=False, dir_okay=True, path_type=Path),
    default=None,
    help="Directory where notebooks are located",
)
@click.option(
    "--publish/--no-publish",
    default=False,
    help="If set, skip notebooks marked with 'publish: false'",
)
def main(notebook: str, input_dir: Path | None, publish: bool) -> None:
    """CLI tool to filter Jupyter notebooks by front-matter metadata."""
    # get Path obj of notebook path
    nb_path = Path(notebook)

    # handle absolute vs relative paths
    if nb_path.is_absolute():
        if input_dir is not None:
            click.secho(
                f"⚠️ Notebook path is absolute; ignoring --input-dir: {input_dir}",
                fg="yellow",
            )
    else:
        if input_dir is not None:
            nb_path = input_dir / notebook

    # check existence
    if not nb_path.exists():
        click.secho(f"❌ Notebook not found: {nb_path}", fg="red", err=True)
        sys.exit(1)

    # apply publish filter if requested
    if publish and not should_publish(nb_path):
        click.secho(f"💤 Skipping unpublished notebook: {nb_path}", fg="yellow")
        sys.exit(1)

    # notebook passes all filters
    click.secho(f"✅ Notebook passes filters: {nb_path}", fg="green")
    sys.exit(0)


if __name__ == "__main__":
    main()
