import ast
from typing import List, Tuple


# Based on:
# - https://github.com/asottile/flake8-2020/blob/v1.7.0/flake8_2020.py#L36
# - https://github.com/marcgibbons/flake8-datetime-import/blob/0.1.0/src/flake8_datetime_import.py#L34  # noqa: E501
class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.errors: List[Tuple[int, int, str]] = []

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        # print(ast.dump(node, include_attributes=True))
        # and run: `flake8 flake8_import_as_module/`

        if node.module == "datetime":
            self.errors.append((node.lineno, node.col_offset, ""))
        if node.module == "time":
            self.errors.append((node.lineno, node.col_offset, ""))

        self.generic_visit(node)
