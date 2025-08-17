class MarkdownConverter:
    def __init__(self, source: str):
        self.css: str = self._load_css(source)
        self.pages: list[str] = self._load_pages(source)

    def _load_css(self, source: str) -> str:
        return ""

    def _load_pages(self, source: str) -> list[str]:
        return []

    def convert(self) -> None:
        pass
