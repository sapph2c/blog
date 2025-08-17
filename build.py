


CSS_PATH = "style.css"


class MarkdownConverter:
    def __init__(self, site_path: str):
        self.css: str = self._load_css(site_path)
        self.pages: list[str] = self._load_pages(site_path)

    def _load_css(self, site_path: str) -> str:
        return get_file_contents(f"{site_path}/{CSS_PATH}")

    def _load_pages(self, site_path: str) -> list[str]:
        
        return []

    def convert(self) -> None:
        pass


def get_file_contents(path: str) -> str:
    with open(path, "r", encoding="locale") as f:
        return f.read()


if __name__ == "__main__":
    site_path = "site"
    c = MarkdownConverter(site_path)
    c.convert()
