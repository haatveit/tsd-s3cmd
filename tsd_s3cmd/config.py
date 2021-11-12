from enum import Enum
import pathlib
from typing import Union

import toml

from tsd_s3cmd.util import get_config_path

CONFIG_DIRECTORY = pathlib.Path(get_config_path())
MAIN_CONFIG_FILE = CONFIG_DIRECTORY / f'{__package__}.toml'
S3CMD_CONFIG_PATTERN = str(CONFIG_DIRECTORY) + "/s3cfg_{project}_{environment}"

class TsdApiHost(Enum):
    prod = "api.tsd.usit.no"
    alt = "alt.api.tsd.usit.no"
    test = "test.api.tsd.usit.no"


def get_s3cmd_config(project: str, environment: str):
    cfg = S3CMD_CONFIG_PATTERN.format(project=project, environment=environment)
    with open(cfg, 'r') as f:
        s3cfg = f.read()
    return s3cfg

def set_s3cmd_config(project: str, environment: str, access_key: str, secret_key: str):
    api_host = TsdApiHost[environment].value
    s3cmd_config = f"""
        host_base = {api_host}
        host_bucket = {api_host}
        bucket_location = us-east-1
        use_https = True
        access_key = {access_key}
        secret_key = {secret_key}
        signature_v2 = False
    """
    cfg = S3CMD_CONFIG_PATTERN.format(project=project, environment=environment)
    with open(cfg, 'w') as f:
        f.write(s3cmd_config)
    return s3cmd_config, cfg

def get_s3_config(config_file: Union[pathlib.Path, str] = MAIN_CONFIG_FILE):
    try:
        config = toml.load(config_file)
    except FileNotFoundError:
        config = {}
    return config

def get_value(key: str, config_file: Union[pathlib.Path, str] = MAIN_CONFIG_FILE) -> Union[str, None]:
    return get_s3_config(config_file=config_file).get(key)

def set_value(*, config_file: Union[pathlib.Path, str] = MAIN_CONFIG_FILE, **kwargs):
    kv: dict = {**kwargs}
    config = get_s3_config(config_file=config_file)
    config.update(kv)
    with open(config_file, 'w') as f:
        toml.dump(config, f)