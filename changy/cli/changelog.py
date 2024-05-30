import typer

from changy import logic

app = typer.Typer()


@app.command()
def create() -> None:
    logic.create_changelog()
