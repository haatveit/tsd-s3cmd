import typer

from tsd_s3cmd.config import set_value
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