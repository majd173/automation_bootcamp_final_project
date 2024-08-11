import requests
import logging
import os
# -----------------------------API CLASSES----------------------------
from orange_hrm.infra.config_provider import ConfigProvider
from orange_hrm.infra.api.api_wrapper import ApiWrapper
from orange_hrm.infra.utilities import Utilities
from orange_hrm.logic.api.entities.admin_contact_details import AdminContactDetails
from orange_hrm.logic.api.entities.employee_object import EmployeeObject
from orange_hrm.logic.api.entities.admin_object import AdminObject


class APIHomePage:
    """
    This class manages API requests for the website.
    It is called home page because it includes all website requests.
    """

    CHANGE_EMPLOYEE_INFO = "pim/employees/7/personal-details"
    CHANGE_ADMIN_DETAILS = "pim/employee/7/contact-details"
    CHANGE_EMPLOYEE_GENDER = "pim/employees/7/personal-details"
    ADD_A_NEW_EMPLOYEE = "pim/employees"
    DELETE_AN_EMPLOYEE = "pim/employees"
    EMPLOYEES_LIST = "pim/employees"
    SEARCH_FOR_AN_EMPLOYEE = "pim/employees"
    ADMIN_DETAILS = "pim/employees/7/personal-details"
    HIRING_MANAGERS = "recruitment/hiring-managers"
    ABOUT = "core/about"
    ADD_A_NEW_POST = "buzz/posts"
    SHARE_A_PHOTO = "buzz/posts"

    def __init__(self, request: ApiWrapper):
        try:
            self._request = request
            self._api = ApiWrapper()
            base_dir = os.path.dirname(os.path.abspath(__file__))
            self._config_file_path = os.path.join(base_dir, '../../orange_hrm.json')
            self._config = ConfigProvider().load_from_file(self._config_file_path)
            self._url = self._config['api_base_url']
        except ImportError:
            logging.error("Can not open orange_hrm.json file.")

    def change_admin_full_name(self, cookie, admin_object: AdminObject):
        """
        This method is used to change employee full name.
        :return: response
        :param: cookie, admin_object
        """
        try:
            logging.info("Sending a put request to change admin full name.")
            response = self._request.put_request(
                f'{self._url}{self.CHANGE_EMPLOYEE_INFO}',
                cookie,
                admin_object.to_dict())
            return response
        except requests.RequestException as e:
            logging.error(f'Put request has not been sent.: {e}')

    def change_admin_city_and_mobile(self, cookie, admin: AdminContactDetails):
        """
        This method is used to change admin city and mobile number.
        :return: response
        :param: cookie, admin
        """
        try:
            logging.info("Sending a put request to change admin city and mobile number.")
            response = self._request.put_request(
                f'{self._url}{self.CHANGE_ADMIN_DETAILS}',
                cookie,
                admin.to_dict())
            return response
        except requests.RequestException as e:
            logging.error(f'Put request has not been sent.: {e}')

    @staticmethod
    def generate_random_employee():
        """
        This method is used to generate an employee.
        :return: An employee object with random values
                    (first name, middle name, last name, employee id).
        """
        try:
            employee = EmployeeObject(Utilities.generate_random_string_only_letters(5),
                                      Utilities.generate_random_string_only_letters(5),
                                      Utilities.generate_random_string_only_letters(5),
                                      Utilities.generate_random_number_by_length(2))
            return employee
        except Exception as e:
            logging.error(f'Can not generate an employee. {e}')

    def add_a_new_employee(self, cookie, employee: EmployeeObject):
        """
        This method is used to add a new employee.
        :return: response
        :param: cookie, employee
        """
        try:
            logging.info("Sending a post request to add a new employee.")
            response = self._request.post_request(
                f'{self._url}{self.ADD_A_NEW_EMPLOYEE}',
                cookie,
                employee.to_dict())
            return response
        except requests.RequestException as e:
            logging.error(f'Post request has not been sent.: {e}')

    def get_active_employees_number(self, cookie):
        """
        This method is used to get active employees number.
        :return: response
        :param: cookie
        """
        try:
            logging.info("Sending a get request to get active employees number.")
            response = self._request.get_request(
                f'{self._url}{self.ABOUT}',
                cookie,
                None)
            return response
        except requests.RequestException as e:
            logging.error(f'Get request has not been sent.: {e}')

    def change_admin_gender(self, cookie, admin_object: AdminObject):
        """
        This method is used to change admin gender.
        :return: response
        :param: cookie, admin
        """
        try:
            logging.info("Sending a put request to change admin gender.")
            response = self._request.put_request(
                f'{self._url}{self.CHANGE_EMPLOYEE_GENDER}',
                cookie,
                admin_object.to_dict())
            return response
        except requests.RequestException as e:
            logging.error(f'Put request has not been sent.: {e}')

    def receive_an_employee_by_id(self, cookie, id):
        """
        This method is used to receive an employee by id.
        :return: employee number.
        :param: cookie, id
        """
        try:
            logging.info("Sending a get request to receive an employee number by his/her id.")
            get_employees_response = self._request.get_request(
                f'{self._url}{self.EMPLOYEES_LIST}',
                cookie,
                None)
            list_of_employees = get_employees_response.json()['data']
            for employee in list_of_employees:
                if employee['employeeId'] == id:
                    return employee['empNumber']
            else:
                logging.error(f'Employee with {id} not found.')
                return None
        except requests.RequestException as e:
            logging.error(f'Get request has not been sent.: {e}')
            return None

    def delete_an_employee(self, cookie, employee_number):
        """
        This method is used to delete an employee by employee number.
        :return: response
        :param: cookie, employee_number
        """
        try:
            logging.info("Sending a delete request to delete an employee.")
            body = {
                "ids": [
                    f'{employee_number}'
                ]
            }
            response = self._request.delete_request(
                f'{self._url}{self.DELETE_AN_EMPLOYEE}',
                cookie,
                body)
            return response
        except requests.RequestException as e:
            logging.error(f'Delete request has not been sent.: {e}')

    def add_a_new_post(self, cookie, post):
        """
        This method is used to add a new post.
        :return: response
        :param: cookie, post
        """
        try:
            logging.info("Sending a post request to add a new post.")
            body = {
                "type": "text",
                "text": post
            }
            response = self._request.post_request(
                f'{self._url}{self.ADD_A_NEW_POST}',
                cookie,
                body)
            return response
        except requests.RequestException as e:
            logging.error(f'Post request has not been sent.: {e}')

    def search_for_an_employee(self, cookie, firstname):
        """
        This method is used to search for an employee by firstname.
        :return: response
        :param: cookie, firstname
        """
        try:
            logging.info("Sending a get request to search for an employee.")
            params = {
                "nameOrId": f'{firstname}',
                "includeEmployees": "onlyCurrent"
            }
            response = self._request.get_request(
                f'{self._url}{self.SEARCH_FOR_AN_EMPLOYEE}',
                cookie,
                params)
            return response
        except requests.RequestException as e:
            logging.error(f'Get request has not been sent.: {e}')

    def share_a_photo_by_post(self, cookie, body):
        """
        This method is used to share a photo by post.
        :return: response
        :param: cookie, body
        """
        try:
            logging.info("Sending a post request to share a photo by post.")
            response = self._request.post_request(
                f'{self._url}{self.SHARE_A_PHOTO}',
                cookie,
                body)
            return response
        except requests.RequestException as e:
            logging.error(f'Post request has not been sent.: {e}')

    def get_hiring_managers(self, cookie, admin_object: AdminObject):
        """
        This method is used to get hiring manager first name.
        :return: hiring manager firstname.
        :param: cookie
        """
        try:
            logging.info("Sending a get request to receive hiring manager first name.")
            params = {
                "limit": 0
            }
            response = self._request.get_request(
                f'{self._url}{self.HIRING_MANAGERS}',
                cookie,
                params)
            # return response.json()['data'][0]['firstName']
            managers_list = response.json()['data']
            for manager in managers_list:
                if manager['firstName'] == admin_object:
                    return manager['firstName']
                else:
                    return None
        except requests.RequestException as e:
            logging.error(f'Get request has not been sent.: {e}')
            return None
