from changy.cli.application import app  # noqa: F401
from changy import logic
import typer


app = typer.Typer()


@app.command()
def create() -> None:
    logic.create_changelog()
