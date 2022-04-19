from uuid import UUID

import requests

from src.config import TEMPLATE_URI


def _call_template_client(uri: str):
    try:
        response = requests.get(uri)
        response.raise_for_status()
        return response.json(), None
    except requests.HTTPError as error:
        if error.response.status_code == 404:
            return {}, None
        return None, {"status_code": error.response.status_code, "message": {}}


def get_template_file(template_name: str):
    return _call_template_client(f"{TEMPLATE_URI}/template/{template_name}")


def get_template_info(tid: UUID):
    return _call_template_client(f"{TEMPLATE_URI}/template/{tid}/info")


def get_template_attachments(template_id: UUID):
    return _call_template_client(f"{TEMPLATE_URI}/template/{template_id}")
