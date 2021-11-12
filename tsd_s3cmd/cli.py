import sys

from importlib.metadata import version as meta_version
from importlib.resources import open_text
from typing import Optional

import typer
from tsd_s3cmd.config import get_value

import tsd_s3cmd.get
import tsd_s3cmd.set

app = typer.Typer()
app.add_typer(tsd_s3cmd.get.app, name="get")
app.add_typer(tsd_s3cmd.set.app, name="set")

@app.command()
def guide():
    """User guide for the software package.
    """
    typer.echo(open_text(__package__, "guide.txt").read())

@app.command()
def register(project: Optional[str] = typer.Argument(get_value("project"))):
    if not project:
        sys.exit("ERROR: project not set.")
    typer.echo(f"Registering client for project {project}")
    pass

@app.command()
def login(project: Optional[str] = typer.Argument(get_value("project"))):
    if not project:
        sys.exit("ERROR: project not set.")
    pass

@app.command()
def version():
    """Display software version information.
    """
    typer.echo(f"{__package__} {meta_version(__package__)}")

if __name__ == "__main__":
    app()