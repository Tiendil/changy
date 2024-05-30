import typer

from changy import logic

app = typer.Typer()


@app.command()
def create(version: str) -> None:
    logic.create_version(version)
