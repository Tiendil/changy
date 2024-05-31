import sys

import typer

from changy import logic, utils

app = typer.Typer()


@app.command()
def create(version: str) -> None:
    with utils.exit_on_exception():
        version_file = logic.create_version(version)

    sys.stdout.write(f"{version_file}\n")
