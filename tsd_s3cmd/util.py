import pathlib

from tsdapiclient.tools import _get_system_config_path

def get_config_path(software: str = __package__) -> pathlib.Path:
    config_path = _get_system_config_path() / software

    if not config_path.exists():
        config_path.mkdir(parents=True)

    return config_path