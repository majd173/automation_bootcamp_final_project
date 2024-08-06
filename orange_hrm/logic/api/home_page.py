import requests
import logging
#-----------------------------API CLASSES----------------------------
from orange_hrm.logic.config_provider import ConfigProvider
from orange_hrm.infra.api.api_wrapper import ApiWrapper
from orange_hrm.logic.api.entities.admin_contact_details import AdminContactDetails
from orange_hrm.logic.api.entities.employee_object import EmployeeObject
from orange_hrm.logic.api.entities.preson_object import PersonObject


class APIHomePage:
    """
    API class for My Info page.
    """

    CHANGE_EMPLOYEE_INFO = "v2/pim/employees/7/personal-details"
    CHANGE_ADMIN_DETAILS = "v2/pim/employee/7/contact-details"
    CHANGE_EMPLOYEE_GENDER = "v2/pim/employees/7/personal-details"
    ADD_A_NEW_EMPLOYEE = "v2/pim/employees"
    DELETE_AN_EMPLOYEE = "v2/pim/employees"
    EMPLOYEES_LIST = "v2/pim/employees"
    ABOUT = "v2/core/about"

    def __init__(self, request: ApiWrapper):
        try:
            self._request = request
            self._api = ApiWrapper()
            self._config = ConfigProvider().load_from_file()
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

    def get_active_employees_number(self, cookie):
        try:
            logging.info("Sending a get request to get ")
            headers = {
                "Cookie": f"{cookie}"
            }
            response = self._request.get_request(
                f'{self._url}{self.ABOUT}',
                headers,
                None)
            return response
        except requests.RequestException as e:
            logging.error(f'Get request has not been sent.: {e}')

    def change_employee_gender(self, cookie, employee: PersonObject):
        try:
            logging.info("Sending a put request to change employee gender.")
            headers = {
                "Cookie": f"{cookie}"
            }
            response = self._request.put_request(
                f'{self._url}{self.CHANGE_EMPLOYEE_GENDER}',
                headers,
                employee.to_dict())
            return response
        except requests.RequestException as e:
            logging.error(f'Put request has not been sent.: {e}')

    def receive_an_employee_by_id(self, cookie, id):
        try:
            logging.info("Sending a get request to receive an employee by id.")
            headers = {
                "Cookie": f"{cookie}"
            }
            get_employees_response = self._request.get_request(
                f'{self._url}{self.EMPLOYEES_LIST}',
                headers,
                None)
            get_employees_response_data = get_employees_response.json()
            list_of_employees = get_employees_response_data['data']
            for employee in list_of_employees:
                if employee['employeeId'] == id:
                    return employee['empNumber']
            else:
                logging.error(f'Employee with {id} not found.')
        except requests.RequestException as e:
            logging.error(f'Get request has not been sent.: {e}')


    def delete_an_employee(self, cookie, employee_number):
        try:
            logging.info("Sending a delete request to delete an employee.")
            headers = {
                "Cookie": f"{cookie}"
            }
            body = {
                "ids": [
                    f'{employee_number}'
                ]
            }
            response = self._request.delete_request(
                f'{self._url}{self.DELETE_AN_EMPLOYEE}',
                headers,
                body)
            return response
        except requests.RequestException as e:
            logging.error(f'Delete request has not been sent.: {e}')


