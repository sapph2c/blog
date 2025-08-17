from builder.converter import MarkdownConverter
import click

@click.command()
@click.option('--source', default='site', help='Directory of Markdown files to convert')
def build(source: str) -> None:
    c = MarkdownConverter(source)
    c.convert()
