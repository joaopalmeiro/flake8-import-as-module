import ast


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.errors = []

    def visit_ImportFrom(self, node):
        pass
