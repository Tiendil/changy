import typer
from changy import utils
from changy import logic

app = typer.Typer()


@app.command()
def create(version: str) -> None:
    with utils.exit_on_exception():
        logic.create_version(version)
