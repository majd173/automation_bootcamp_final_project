import requests
import logging
#-----------------------------API CLASSES----------------------------
from orange_hrm.infra.api.config_provider import ConfigProvider
from orange_hrm.infra.api.api_wrapper import ApiWrapper
from orange_hrm.logic.api.enums.preson_object import PersonObject


class APIHomePage:
    """
    API class for My Info page.
    """

    CHANGE_EMPLOYEE_INFO = "api/v2/pim/employees/7/personal-details"

    def __init__(self, request: ApiWrapper):
        try:
            self._request = request
            self._api = ApiWrapper()
            self._config = ConfigProvider().load_from_file(
                r'C:\Users\Admin\Desktop\Automation_bootcamp\orange_hrm\orange_hrm.json')
            self._url = self._config['api_base_url']
        except ImportError:
            logging.error("Can not open orange_hrm.json file.")

    def change_employee_full_name(self, cookie, person_object: PersonObject):
        """
        This function is used to change employee full name.
        """
        try:
            logging.info("Sending a put request to change employee full name.")
            headers = {
                "Cookie": f"{cookie}; {self._config}['permanent_cookie']"
            }

            response = self._request.put_request(
                f'{self._url}{self.CHANGE_EMPLOYEE_INFO}',
                headers,
                person_object.to_dict())
            return response

        except requests.RequestException as e:
            logging.error(f'Put request has not been sent.: {e}')
