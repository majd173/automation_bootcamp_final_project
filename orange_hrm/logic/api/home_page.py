import requests
import logging
#-----------------------------API CLASSES----------------------------
from orange_hrm.infra.api.config_provider import ConfigProvider
from orange_hrm.infra.api.api_wrapper import ApiWrapper
from orange_hrm.logic.api.enums.admin_contact_details import AdminContactDetails
from orange_hrm.logic.api.enums.employee_object import EmployeeObject
from orange_hrm.logic.api.enums.preson_object import PersonObject


class APIHomePage:
    """
    API class for My Info page.
    """

    CHANGE_EMPLOYEE_INFO = "v2/pim/employees/7/personal-details"
    CHANGE_ADMIN_DETAILS = "v2/pim/employee/7/contact-details"
    ADD_A_NEW_EMPLOYEE = "v2/pim/employees"

    def __init__(self, request: ApiWrapper):
        try:
            self._request = request
            self._api = ApiWrapper()
            self._config = ConfigProvider().load_from_file(
                r'C:\Users\Admin\Desktop\Automation_bootcamp_Final_project\orange_hrm\orange_hrm.json')
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
                "Cookie": f'{cookie}'
            }
            response = self._request.put_request(
                f'{self._url}{self.CHANGE_EMPLOYEE_INFO}',
                headers,
                person_object.to_dict())
            print(f'{self._url}{self.CHANGE_EMPLOYEE_INFO}')
            return response

        except requests.RequestException as e:
            logging.error(f'Put request has not been sent.: {e}')

    def change_admin_city_and_mobile(self, cookie, admin: AdminContactDetails):
        try:
            logging.info("Sending a put request to change admin city and mobile number.")
            headers = {
                "Cookie": f"{cookie}"
            }
            response = self._request.put_request(
                f'{self._url}{self.CHANGE_ADMIN_DETAILS}',
                headers,
                admin.to_dict())
            return response
        except requests.RequestException as e:
            logging.error(f'Put request has not been sent.: {e}')

    def add_a_new_employee(self, cookie, employee: EmployeeObject):
        try:
            logging.info("Sending a post request to add a new employee.")
            headers = {
                "Cookie": f"{cookie}"
            }
            response = self._request.post_request(
                f'{self._url}{self.ADD_A_NEW_EMPLOYEE}',
                headers,
                employee.to_dict())
            return response
        except requests.RequestException as e:
            logging.error(f'Post request has not been sent.: {e}')
