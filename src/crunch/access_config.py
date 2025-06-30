"""
This module handles all config used by the crunch package, as well as most tests.
"""
import tomllib
from pathlib import Path


ROOT_PATH = Path(__file__).resolve().parent.parent.parent


class GlobalConfig:
    """
    A singleton config object that contains both config.toml and config_template.toml layered.

    File read is performed on object init.
    """
    _singleton = None

    def __init__(self):
        with open(ROOT_PATH / "config_template.toml", "rb") as f:
            self._d = tomllib.load(f)
        
        if (config_path := ROOT_PATH / "config.toml").exists():
            with open(config_path, "rb") as f:
                new_d = tomllib.load(f)
            for section, values in new_d.items():
                self._d[section].update(values)

    def __new__(cls):
        if not cls._singleton:
            cls._singleton = super(GlobalConfig, cls).__new__(cls)
        return cls._singleton

    def __getitem__(self, item):
        return self._d[item]
