import urllib3
import requests
from requests.auth import HTTPBasicAuth

from proxy_api import url as public_url

urllib3.disable_warnings()

url = "https://127.0.0.1:12001"
auth_username = "prov_user"
auth_password = "prov_password"

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

def get_prov_of_patient(id):
    # send a request to the service.
    response = session.get(
        url = f"{url}/provenance/service",
        params={
            "target": f"{public_url}/v1/patient/{id}"
        },
        auth = HTTPBasicAuth(auth_username, auth_password),
        headers = {
            "Accept": "application/json"
        },
        verify = False
    )

    if response.status_code < 200 or response.status_code > 299:
        raise ConnectionError(f"Wrong status code {response.status_code}")

    return response.text
