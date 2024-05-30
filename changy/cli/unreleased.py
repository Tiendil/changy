from changy.cli.application import app  # noqa: F401
from changy import logic
import typer

from changy.cli import version


app = typer.Typer()


@app.command()
def create() -> None:
    logic.create_unreleased()


@app.command()
def approve() -> None:
    logic.approve_unreleased()
