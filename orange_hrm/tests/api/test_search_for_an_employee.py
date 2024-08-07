import logging
import unittest
from orange_hrm.infra.utilities import Utilities
from orange_hrm.logic.config_provider import ConfigProvider
#-----------------------------API CLASSES----------------------------
from orange_hrm.logic.api.home_page import APIHomePage
from orange_hrm.infra.api.api_wrapper import ApiWrapper
from orange_hrm.logic.api.entities.employee_object import EmployeeObject
#-----------------------------UI CLASSES-----------------------------
from orange_hrm.logic.ui.log_in_page import LogInPage
from orange_hrm.infra.ui.browser_wrapper import BrowserWrapper


class TestSearchForAnEmployee(unittest.TestCase):

    def setUp(self):
        """
        This method initializes driver and loads config file.
        """
        logging.info("----------------Test Started----------------")
        # ARRANGE
        self._config = ConfigProvider().load_from_file()
        self._driver = BrowserWrapper().get_driver()
        self._api = ApiWrapper()

    def tearDown(self):
        """
        This method closes driver.
        """
        self._driver.close()
        logging.info("----------------Test Completed----------------\n")

    def test_search_for_an_employee(self):
        """
        This method tests adding an employee and searching for him/her.
        Test case: TC-11 / Search for an employee.
        """
        # ACT
        self._login_page = LogInPage(self._driver)
        cookie = self._login_page.valid_login_flow()
        employee = EmployeeObject(Utilities.generate_random_number_by_length(3),
                                  Utilities.generate_random_string_only_letters(7),
                                  Utilities.generate_random_string_only_letters(7),
                                  Utilities.generate_random_string_only_letters(7))
        self._api_home_page = APIHomePage(self._api)
        self._api_home_page.add_a_new_employee(cookie, employee)
        added_employee_response = self._api_home_page.search_for_an_employee(cookie, employee.firstname)
        # ASSERT
        self.assertTrue(added_employee_response.ok,
                        "Request has not been accepted.")
        self.assertEqual(added_employee_response.status_code, 200,
                         "Status code is not 200.")
        self.assertEqual(added_employee_response.json()['data'][0]['firstName'], employee.firstname,
                         "Received employee firstname is not correct.")


if __name__ == '__main__':
    unittest.main()
