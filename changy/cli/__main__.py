from changy import logic, utils
from changy.cli import changelog, unreleased, version
from changy.cli.application import app  # noqa: F401

app.add_typer(version.app, name="version")
app.add_typer(unreleased.app, name="unreleased")
app.add_typer(changelog.app, name="changelog")


@app.command()
def init() -> None:
    with utils.exit_on_exception():
        logic.init()


app()
