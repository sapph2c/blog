from pathlib import Path

import markdown


CSS_PATH = "style.css"
OUTPUT_DIR = "html"
SITE_PATH = "site"


class MarkdownConverter:
    def __init__(self, site_path: str):
        self.site_path: str = site_path
        self.css: str = self._load_css(site_path)
        self.pages: list[str] = self._load_pages(site_path)

    def _load_css(self, site_path: str) -> str:
        return get_file_contents(f"{site_path}/{CSS_PATH}")

    def _load_pages(self, site_path: str) -> list[str]:
        return get_all_file_paths(site_path)

    def convert(self) -> None:
        for path in self.pages:
            content = get_file_contents(path)
            html = markdown.markdown(content)
            output_file = Path(convert_path(self.site_path, path))
            build_page(output_file, html, self.css)

def get_file_contents(path: str) -> str:
    with open(path, "r", encoding="locale") as f:
        return f.read()


def get_all_file_paths(path: str) -> list[str]:
    return [str(path) for path in Path(path).rglob("*.md")]


def convert_path(base, path: str) -> str:
    # this code is gross but works! Feel free to PR and present an idiomatic way of doing this
    baseless = path[len(base):]
    md_to_html = f"{baseless[:-2]}html"
    return f"{OUTPUT_DIR}{md_to_html}"


def build_page(output_file: Path, html: str, css: str):
    output_file.parent.mkdir(exist_ok=True, parents=True)
    head = f"<head><style>{css}</style></head>"
    output_file.write_text(f"{head}\n<body>{html}\n</body>")


if __name__ == "__main__":
    c = MarkdownConverter(SITE_PATH)
    c.convert()
