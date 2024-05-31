import sys

import typer

from changy import logic, utils

app = typer.Typer()


@app.command()
def create(version: str) -> None:
    with utils.exit_on_exception():
        version_file = logic.create_version(version)

    sys.stdout.write(f"{version_file}\n")


@app.command()
def show(version: str) -> None:
    with utils.exit_on_exception():
        body = logic.show_version_changes(version)

    sys.stdout.write(body)
