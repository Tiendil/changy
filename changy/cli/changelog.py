import typer

from changy import logic, utils

app = typer.Typer()


@app.command()
def create() -> None:
    with utils.exit_on_exception():
        logic.create_changelog()
