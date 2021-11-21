import json

import requests


def get(link: str) -> requests.Response:
    """
    Perform GET request and parse response.

    :param link: http address
    :type link: str
    :return: full response object, response data, and employee data
    :rtype: requests.Response
    """
    # Requests adds header 'User-Agent': 'python-requests/2.26.0'.
    # Seems server don't want to work with automated requests
    # and returns 406 Not Acceptable.
    return requests.get(link, headers={"User-Agent": ""})


def post(link: str, data: dict = None) -> requests.Response:
    """
    Perform POST request and parse response.

    :param link: http address
    :type link: str
    :param data: payload for request
    :type data: dict
    :return: full response object, response data, and employee data
    :rtype: requests.Response
    """
    # Requests adds header 'User-Agent': 'python-requests/2.26.0'.
    # Seems server don't want to work with automated requests
    # and returns 406 Not Acceptable.
    return requests.post(link, data=data, headers={"User-Agent": ""})


def parse_json(full_response: requests.Response) -> dict:
    """
    Parse response object.

    :param full_response: response object
    :type full_response: requests.Response
    :return: parsed response data
    :rtype: dict
    """
    try:
        return json.loads(full_response.text)
    except json.JSONDecodeError:
        # If server returned something unexpected we want to know
        # what happened.
        print((f"Response status: {full_response.status_code}.\n"
               f"Response text: {full_response.text}"))
        raise
