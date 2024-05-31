import typer

from changy import logic, utils

app = typer.Typer()


@app.command()
def create() -> None:
    with utils.exit_on_exception():
        logic.create_unreleased()


@app.command()
def approve() -> None:
    with utils.exit_on_exception():
        logic.approve_unreleased()
