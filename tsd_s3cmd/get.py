from typing import Optional
from click.core import Option
import typer

from tsd_s3cmd.config import get_s3_config, get_s3cmd_config, get_value

app = typer.Typer()

@app.command()
def config():
    """Show the currently applied configuration."""
    typer.echo(get_s3_config())

@app.command()
def environment():
    """See which TSD environment is set for use.
    """
    typer.echo(get_value("environment"))

@app.command()
def project():
    """See which TSD project will be used.
    """
    typer.echo(get_value("project"))

@app.command()
def s3cfg(
    project: Optional[str] = get_value("project"),
    environment: Optional[str] = get_value("environment"),
):
    """See the s3cmd configuration ("s3cfg") for a project in a given environment.

    Args:

        project (Optional[str], optional): Project to use. Defaults to set project.

        environment (Optional[str], optional): Environment to use. Defaults to set environment.
    """
    try:
        typer.echo(get_s3cmd_config(project=project, environment=environment))
    except FileNotFoundError:
        typer.echo(f"No s3cfg set for project '{project}' in environment '{environment}'")