import logging

import requests


class ApiWrapper:
    """
    This class manages types of requests can be used in logic classes.
    """

    def __init__(self):
        self._request = None

    def get_request(self, url, headers=None, params=None, body=None):
        try:
            return requests.get(url, headers=headers, params=params, json=body)
        except requests.exceptions.RequestException as e:
            logging.error(e)

    def post_request(self, url, headers=None, body=None):
        try:
            return requests.post(url, headers=headers, json=body)
        except requests.exceptions.RequestException as e:
            logging.error(e)

    def put_request(self, url, headers=None, body=None):
        try:
            return requests.put(url, headers=headers, json=body)
        except requests.exceptions.RequestException as e:
            logging.error(e)

    def delete_request(self, url, headers=None, data=None):
        try:
            return requests.delete(url, headers=headers, json=data)
        except requests.exceptions.RequestException as e:
            logging.error(e)
