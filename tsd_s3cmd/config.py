import pathlib
from typing import Union

import toml

from tsdapiclient.configurer import read_config, write_config, update_config
from tsdapiclient.tools import get_config_path

DEFAULT_CONFIG_PATH = pathlib.Path(get_config_path()) / 's3.toml'

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