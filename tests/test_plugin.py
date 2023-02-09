import ast
from typing import Set

import pytest

from flake8_import_as_module import Plugin


def run_plugin(code: str) -> Set[str]:
    # Based on:
    # - https://github.com/marcgibbons/flake8-datetime-import/blob/0.1.0/tests/test_plugin.py#L8  # noqa: E501
    # - https://docs.python.org/3.7/library/typing.html#typing.Set
    tree = ast.parse(code)
    plugin = Plugin(tree)

    return {f"{line}:{col}: {msg}" for line, col, msg, _ in plugin.run()}


@pytest.mark.parametrize(
    "code",
    [
        "from pandas import DataFrame",
    ],
)
def test_IM001_from_pandas_import(code):
    result = run_plugin(code)
    assert result == {
        "1:0: IM001 `from pandas import ...` is unconventional. "
        "`pandas` should be imported as a module."
    }
