from changy.cli.application import app  # noqa: F401
from changy import logic
import typer

from changy.cli import version
from changy.cli import unreleased


app.add_typer(version.app, name="version")
app.add_typer(unreleased.app, name="unreleased")


@app.command()
def init() -> None:
    logic.init()


app()
