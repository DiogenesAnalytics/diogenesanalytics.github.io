"""Filters for filtering on Jupyter notebook YAML front matter."""

from pathlib import Path

import nbformat
import yaml
from typinig import Any
from typinig import Dict


def parse_front_matter(nb_path: Path) -> Dict[str, Any]:
    """Parse YAML front-matter from the first cell of a Jupyter notebook."""
    # open notebook
    nb = nbformat.read(nb_path, as_version=4)  # type: ignore

    # no cells at all ...
    if not nb.cells:
        return {}

    # get first cell
    first_cell = nb.cells[0]

    # check the type is correct
    if first_cell.cell_type not in ("raw", "markdown"):
        return {}

    # concat to string
    text: str = "".join(first_cell.source)

    # make sure it's front matter
    if not text.startswith("---"):
        return {}

    # finally get the YAML out
    try:
        return yaml.safe_load(text.split("---", 2)[1]) or {}
    except Exception:
        return {}


def should_publish(nb_path: Path) -> bool:
    """Return True if notebook should be published based on front-matter."""
    front_matter = parse_front_matter(nb_path)
    return front_matter.get("publish") is not False
