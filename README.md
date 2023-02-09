# flake8-import-as-module

A [Flake8](https://flake8.pycqa.org/) plugin to check if specific packages are imported as modules.

## References

- https://docs.python.org/3.7/tutorial/modules.html
- https://stackoverflow.com/a/49072655
- https://github.com/marcgibbons/flake8-datetime-import
- https://github.com/joaopalmeiro/flake8-import-conventions
- https://github.com/asottile/flake8-2020

## Development

```bash
poetry install --with dev
```

```bash
poetry shell
```

```bash
pytest tests/ -v
```

If changes are not reflected in VS Code after changing something in the package, close it and open it again.

## Deployment

```bash
poetry check
```

```bash
poetry version minor
```

or

```bash
poetry version patch
```

Commit the change in the `pyproject.toml` file.

```bash
git tag
```

```bash
git tag "v$(poetry version --short)"
```

```bash
git push origin "v$(poetry version --short)"
```

## Notes

- https://docs.python.org/3.7/library/ast.html#abstract-grammar
- https://github.com/pycqa/isort/wiki/isort-Plugins + https://github.com/Microsoft/vscode-python + https://marketplace.visualstudio.com/items?itemName=ms-python.isort
- https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter
- https://github.com/john-hen/Flake8-pyproject
- https://flake8.pycqa.org/en/5.0.0/user/options.html
- https://github.com/tylerwince/flake8-bandit
- https://github.com/m-burst/flake8-pytest-style
- `poetry add mypy black pytest Flake8-pyproject flake8-bandit flake8-pytest-style --group dev`
- `poetry add isort@^5.11.5 --group dev`
- `flake8 --version`
- https://www.flake8rules.com/
- https://github.blog/2020-05-12-create-and-push-tags-in-the-latest-github-desktop-2-5-release/
