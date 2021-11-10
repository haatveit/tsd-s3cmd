import typer

from tsd_s3cmd.config import get_s3_config, get_value

app = typer.Typer()

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