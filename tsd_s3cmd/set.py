import typer

from tsd_s3cmd.config import get_value, set_value, set_s3cmd_config
from tsd_s3cmd.types import TsdEnvironment

app = typer.Typer()

@app.command()
def environment(environment: TsdEnvironment):
    """Set which TSD environment to use.

    Args:
        environment (TsdEnvironment): the TSD environment name
    """
    set_value(environment=environment.value)

@app.command()
def project(project: str):
    """Set which TSD project to use.

    Args:
        project (str): the project name
    """
    set_value(project=project)

@app.command()
def s3cfg(project=get_value("project"), environment=get_value("environment")):
    access_key = typer.prompt(f"S3 access key for {project}")
    secret_key = typer.prompt(f"S3 secret key for {project}")
    config, file = set_s3cmd_config(
        project=project,
        environment=environment,
        access_key=access_key,
        secret_key=secret_key,
    )
    typer.echo(f"The following configuration was written to {file}:\n{config}")