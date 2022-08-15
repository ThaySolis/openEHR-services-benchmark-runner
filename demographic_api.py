import urllib3
import requests
from requests.auth import HTTPBasicAuth

import benchmark_utils

urllib3.disable_warnings()

url = "https://127.0.0.1:12002"
auth_username = "demographic_user"
auth_password = "demographic_password"

session = requests.Session()

def clear_statistics():
    # send a request to the service.
    response = session.delete(
        url = f"{url}/usage_statistics",
        headers = {
            "Accept": "application/json"
        },
        verify = False
    )

    if response.status_code < 200 or response.status_code > 299:
        raise ConnectionError(f"Wrong status code {response.status_code}")

def get_statistics():
    # send a request to the service.
    response = session.get(
        url = f"{url}/usage_statistics",
        headers = {
            "Accept": "application/json"
        },
        verify = False
    )

    if response.status_code < 200 or response.status_code > 299:
        raise ConnectionError(f"Wrong status code {response.status_code}")

    return response.json()

def create_patient(data):
    # send a request to the service.
    response = session.post(
        url = f"{url}/v1/patient",
        auth = HTTPBasicAuth(auth_username, auth_password),
        headers = {
            "Accept": "application/json"
        },
        json = data,
        verify = False
    )

    if response.status_code < 200 or response.status_code > 299:
        raise ConnectionError(f"Wrong status code {response.status_code}")

    return response.headers.get("etag")

def update_patient(previous_id, data):
    # send a request to the service.
    response = session.put(
        url = f"{url}/v1/patient/{benchmark_utils.extract_versioned_object_id_from_version_id(previous_id)}",
        auth = HTTPBasicAuth(auth_username, auth_password),
        headers = {
            "Accept": "application/json",
            "If-Match": previous_id
        },
        json = data,
        verify = False
    )

    if response.status_code < 200 or response.status_code > 299:
        raise ConnectionError(f"Wrong status code {response.status_code}")

    return response.headers.get("etag")

def get_patient(id):
    # send a request to the service.
    response = session.get(
        url = f"{url}/v1/patient/{id}",
        auth = HTTPBasicAuth(auth_username, auth_password),
        headers = {
            "Accept": "application/json"
        },
        verify = False
    )

    if response.status_code < 200 or response.status_code > 299:
        raise ConnectionError(f"Wrong status code {response.status_code}")

    return response.json