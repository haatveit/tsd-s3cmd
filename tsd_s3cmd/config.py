from enum import Enum
import pathlib
from typing import Union

import toml

from tsdapiclient.configurer import read_config, write_config, update_config
from tsdapiclient.tools import get_config_path

DEFAULT_CONFIG_PATH = pathlib.Path(get_config_path()) / 's3.toml'

class TsdApiHost(Enum):
    prod = "api.tsd.usit.no"
    alt = "alt.api.tsd.usit.no"
    test = "test.api.tsd.usit.no"

def get_s3cmd_config(project: str, environment: str):
    s3cmd_config_file = pathlib.Path(get_config_path()) / f"s3cfg_{project}_{environment}"
    with open(s3cmd_config_file, 'r') as f:
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
    s3cmd_config_file = pathlib.Path(get_config_path()) / f"s3cfg_{project}_{environment}"
    with open(s3cmd_config_file, 'w') as f:
        f.write(s3cmd_config)
    return s3cmd_config, s3cmd_config_file

def get_s3_config(config_file: Union[pathlib.Path, str] = DEFAULT_CONFIG_PATH):
    try:
        config = toml.load(config_file)
    except FileNotFoundError:
        config = {}
    return config

def get_value(key: str, config_file: Union[pathlib.Path, str] = DEFAULT_CONFIG_PATH) -> Union[str, None]:
    return get_s3_config().get(key)

def set_value(*, config_file: Union[pathlib.Path, str] = DEFAULT_CONFIG_PATH, **kwargs):
    kv: dict = {**kwargs}
    config = get_s3_config(config_file=config_file)
    config.update(kv)
    with open(config_file, 'w') as f:
        toml.dump(config, f)