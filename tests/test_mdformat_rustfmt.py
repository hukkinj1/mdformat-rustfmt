from pathlib import Path

from markdown_it.utils import read_fixture_file
import mdformat
import pytest

TEST_CASES = read_fixture_file(Path(__file__).parent / "data" / "fixtures.md")


@pytest.mark.parametrize(
    "line,title,text,expected", TEST_CASES, ids=[f[1] for f in TEST_CASES]
)
def test_fixtures(line, title, text, expected):
    """Test fixtures in tests/data/fixtures.md."""
    md_new = mdformat.text(text, codeformatters={"rust"})
    if md_new != expected:
        print("Formatted (unexpected) Markdown below:")
        print(md_new)
    assert md_new == expected


def test_rustfmt_error(capfd):
    """Test that any prints by rustfmt go to devnull."""
    unformatted_md = """~~~rust
blaalbal.ablaa
~~~
"""
    formatted_md = """```rust
blaalbal.ablaa
```
"""
    result = mdformat.text(unformatted_md, codeformatters={"rust"})
    captured = capfd.readouterr()
    assert not captured.err
    assert not captured.out
    assert result == formatted_md
