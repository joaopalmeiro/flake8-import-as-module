from typing import Dict

from pytablewriter import MarkdownTableWriter

from flake8_import_as_module.constants import CODE_PREFIX, PACKAGES
from flake8_import_as_module.utils import generate_code, generate_description

# Follow the same order as in name2asname:
package2name: Dict[str, str] = {
    "altair": "Altair",
    "pandas": "pandas",
}
package2url: Dict[str, str] = {
    "altair": "https://altair-viz.github.io/",
    "pandas": "https://pandas.pydata.org/",
}


if __name__ == "__main__":
    # https://github.com/thombashi/pytablewriter#write-a-markdown-table
    # https://pytablewriter.readthedocs.io/en/latest/pages/reference/writers/text/markup/md.html
    # https://pytablewriter.readthedocs.io/en/latest/pages/reference/writers/text/markup/md.html#pytablewriter.MarkdownTableWriter.write_table
    values = [
        [
            f"[{package2name[package]}]({package2url[package]})",
            generate_code(CODE_PREFIX, code_number),
            generate_description(package),
        ]
        for code_number, package in enumerate(PACKAGES, start=1)
    ]

    writer = MarkdownTableWriter(
        # https://github.com/thombashi/pytablewriter/blob/v0.64.2/pytablewriter/writer/text/_markdown.py#L152
        headers=["Package", "Code", "Description"],
        value_matrix=values,
    )
    writer.write_table(flavor="github")
