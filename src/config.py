import json


class UseDotNotation(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setattr__
    __delattr__ = dict.__delattr__


def _load_json(file_path: str) -> dict:
    with open(file_path) as file:
        config_parameters = file.read()

    config_default = json.loads(config_parameters)
    return UseDotNotation(config_default)


SMTP_CONFIG = _load_json("config/smtp_config.json")
TEMPLATE_URI = "http://localhost:5000"
