import logging
import unittest
from orange_hrm.logic.config_provider import ConfigProvider
#-----------------------------API CLASSES----------------------------
from orange_hrm.logic.api.home_page import APIHomePage
from orange_hrm.infra.api.api_wrapper import ApiWrapper
from orange_hrm.infra.utilities import Utilities
from orange_hrm.logic.api.entities.employee_object import EmployeeObject
#-----------------------------UI CLASSES-----------------------------
from orange_hrm.logic.ui.log_in_page import LogInPage
from orange_hrm.logic.ui.home_page import UiHomePage
from orange_hrm.infra.ui.browser_wrapper import BrowserWrapper
from orange_hrm.logic.ui.pim_page import UiPimPage


class TestAddANewEmployee(unittest.TestCase):


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


    def test_add_a_new_employee(self):
        """
        This method tests add a new employee.
        Test case: TC-06 / Add a new employee.
        """
        # ACT
        self._login_page = LogInPage(self._driver)
        cookie = self._login_page.valid_login_flow()
        self._api_home_page = APIHomePage(self._api)
        employee = EmployeeObject(Utilities.generate_random_number_by_length(3),
                                  Utilities.generate_random_string_only_letters(7),
                                  Utilities.generate_random_string_only_letters(7),
                                  Utilities.generate_random_string_only_letters(7))
        self._api_home_page.add_a_new_employee(cookie, employee)
        self._home_page = UiHomePage(self._driver)
        self._home_page.click_pim_button()
        self._pim_page = UiPimPage(self._driver)
        # ASSERT
        self.assertIn(employee.firstname, self._pim_page.check_employee_existence())
        self.assertIn(employee.lastname, self._pim_page.check_employee_existence())
        self.assertIn(employee.middle_name, self._pim_page.check_employee_existence())
        self.assertIn(employee.id, self._pim_page.check_employee_existence())



if __name__ == '__main__':
    unittest.main()
