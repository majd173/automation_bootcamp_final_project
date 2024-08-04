import json
import requests
from orange_hrm.infra.api.logger_setup import LoggingSetup

class ApiWrapper:
    """
    This class manages types of requests can be used in logic classes.
    """

    def __init__(self):
        self._request = None


    def get_request(self, url, body=None):
        return requests.get(url, json=body)

    def post_request(self, url, headers=None, body=None):
        return requests.post(url, headers=headers, json=body)

    def put_request(self, url, headers=None, body=None):
        try:
            return requests.put(url, headers=headers, json=body)
        except requests.exceptions.RequestException as e:
            print(e)


    def delete_request(self, url, data=None):
        return requests.delete(url, json=data)



