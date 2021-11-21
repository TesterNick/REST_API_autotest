import json

import requests


def get(link: str) -> tuple[requests.Response, dict, dict]:
    # Requests adds header 'User-Agent': 'python-requests/2.26.0'.
    # Seems server don't want to work with automated requests
    # and returns 406 Not Acceptable.
    full_response = requests.get(link, headers={"User-Agent": ""})
    response_data, employee_data = parse_json(full_response)
    return full_response, response_data, employee_data


def post(link: str, data: dict = None) -> tuple[requests.Response, dict, dict]:
    # Requests adds header 'User-Agent': 'python-requests/2.26.0'.
    # Seems server don't want to work with automated requests
    # and returns 406 Not Acceptable.
    full_response = requests.post(link, data=data, headers={"User-Agent": ""})
    response_data, employee_data = parse_json(full_response)
    return full_response, response_data, employee_data


def parse_json(full_response: requests.Response) -> tuple[dict, dict]:
    try:
        response_data = json.loads(full_response.text)
        employee_data = response_data["data"]
        return response_data, employee_data
    except json.JSONDecodeError:
        # If server returned something unexpected we want to know
        # what happened.
        print((f"Response status: {full_response.status_code}.\n"
               f"Response text: {full_response.text}"))
        raise
