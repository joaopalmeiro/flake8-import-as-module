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
    # ("code",),
    # https://github.com/m-burst/flake8-pytest-style/blob/master/docs/rules/PT006.md
    "code",
    [
        "from altair import Chart, X, Y",
        "from altair import Chart",
        "from altair import X",
        "from altair import Y",
    ],
)
def test_from_altair_import(code):
    result = run_plugin(code)
    assert result == {
        "1:0: IM001 `from altair import ...` is unconventional. "
        "`altair` should be imported as a module."
    }


@pytest.mark.parametrize(
    "code",
    [
        "from pandas import DataFrame, Series",
        "from pandas import DataFrame",
        "from pandas import Series",
    ],
)
def test_from_pandas_import(code):
    result = run_plugin(code)
    assert result == {
        "1:0: IM002 `from pandas import ...` is unconventional. "
        "`pandas` should be imported as a module."
    }
