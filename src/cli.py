# src/cli.py
import click
from .store import add_item, list_items, mark_done

@click.group()
def cli():
    """Todo CLI - add, list, done"""
    pass

@cli.command()
@click.argument("text", nargs=-1)
def add(text):
    """Add a todo: todo add Buy milk"""
    if not text:
        click.echo("Error: no text provided", err=True)
        raise SystemExit(2)
    text = " ".join(text)
    item = add_item(text)
    click.echo(f"Added: {item['text']} (id: {item['id']})")

@cli.command(name="list")
def _list():
    """List all todos"""
    items = list_items()
    if not items:
        click.echo("No todos found.")
        return
    for i, it in enumerate(items, 1):
        status = "✓" if it.get("done") else " "
        click.echo(f"{i}. [{status}] {it['text']}")

@cli.command()
@click.argument("index", type=int)
def done(index):
    """Mark todo done by 1-based index: todo done 2"""
    try:
        item = mark_done(index - 1)
        click.echo(f"Marked done: {item['text']}")
    except IndexError:
        click.echo("Error: invalid index", err=True)
        raise SystemExit(2)

if __name__ == "__main__":
    cli()