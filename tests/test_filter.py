"""Test for filter-notebook CLI tool."""

import textwrap
from pathlib import Path

import nbformat
import pytest
from filter_notebook.filter import parse_front_matter
from filter_notebook.filter import should_publish


def write_notebook_raw(path: Path, raw_text: str) -> None:
    """Write a notebook with a single raw cell containing given text."""
    nb = nbformat.v4.new_notebook()  # type: ignore
    nb.cells.append(nbformat.v4.new_raw_cell(raw_text))  # type: ignore
    nbformat.write(nb, path)  # type: ignore


@pytest.fixture(scope="function")
def nb_publish_true(tmp_path: Path) -> Path:
    """Single cell notebook with `publish: true` front-matter."""
    file = tmp_path / "pub_true.ipynb"
    write_notebook_raw(
        file,
        textwrap.dedent(
            """\
            ---
            title: Test Publish True
            publish: true
            ---
        """
        ),
    )
    return file


@pytest.fixture(scope="function")
def nb_publish_false(tmp_path: Path) -> Path:
    """Single cell notebook with `publish: false` front-matter."""
    file = tmp_path / "pub_false.ipynb"
    write_notebook_raw(
        file,
        textwrap.dedent(
            """\
            ---
            title: Test Publish False
            publish: false
            ---
        """
        ),
    )
    return file


@pytest.fixture(scope="function")
def nb_no_publish_field(tmp_path: Path) -> Path:
    """Single cell notebook with NO publish attribute in front-matter."""
    file = tmp_path / "no_pub.ipynb"
    write_notebook_raw(
        file,
        textwrap.dedent(
            """\
            ---
            title: Test Publish Default (Missing)
            ---
        """
        ),
    )
    return file


@pytest.fixture(scope="function")
def nb_empty(tmp_path: Path) -> Path:
    """Notebook with zero cells (empty notebook)."""
    file = tmp_path / "empty.ipynb"
    nb = nbformat.v4.new_notebook()  # type: ignore
    nbformat.write(nb, file)  # type: ignore
    return file


@pytest.mark.filter
def test_parse_front_matter_publish_true(nb_publish_true: Path) -> None:
    """Test correct dict for notebook with publish: true."""
    fm = parse_front_matter(nb_publish_true)
    assert fm.get("publish") is True
    assert fm.get("title") == "Test Publish True"


@pytest.mark.filter
def test_parse_front_matter_publish_false(nb_publish_false: Path) -> None:
    """Test correct dict for notebook with publish: false."""
    fm = parse_front_matter(nb_publish_false)
    assert fm.get("publish") is False
    assert fm.get("title") == "Test Publish False"


@pytest.mark.filter
def test_parse_front_matter_no_publish(nb_no_publish_field: Path) -> None:
    """Test dict without 'publish' for notebook missing the field."""
    fm = parse_front_matter(nb_no_publish_field)
    assert "publish" not in fm
    assert fm.get("title") == "Test Publish Default (Missing)"


@pytest.mark.filter
def test_should_publish_true(nb_publish_true: Path) -> None:
    """Test for notebooks with publish: true attribute."""
    assert should_publish(nb_publish_true) is True


@pytest.mark.filter
def test_should_publish_default(nb_no_publish_field: Path) -> None:
    """Test for notebooks with NO publish attribute."""
    assert should_publish(nb_no_publish_field) is True


@pytest.mark.filter
def test_should_publish_false(nb_publish_false: Path) -> None:
    """should_publish returns False for notebooks with publish: false."""
    assert should_publish(nb_publish_false) is False


@pytest.mark.filter
def test_should_publish_empty(nb_empty: Path) -> None:
    """Test for empty notebooks."""
    assert should_publish(nb_empty) is True
