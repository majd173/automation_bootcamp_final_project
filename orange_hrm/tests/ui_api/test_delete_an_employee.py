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
from orange_hrm.logic.ui.my_info_page import UiMyInfoPage
from orange_hrm.logic.ui.pim_page import UiPimPage


class TestDeleteAnEmployee(unittest.TestCase):

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

    def test_delete_an_employee(self):
        self._login_page = LogInPage(self._driver)
        cookie = self._login_page.valid_login_flow()
        self._api_home_page = APIHomePage(self._api)
        employee = EmployeeObject(Utilities.generate_random_string_only_letters(5),
                                  Utilities.generate_random_string_only_letters(5),
                                  Utilities.generate_random_string_only_letters(5),
                                  Utilities.generate_random_number_by_length(2))
        self._api_home_page.add_a_new_employee(cookie, employee)
        self._api_home_page.receive_an_employee_by_id(cookie, employee.id)
        employee_number = self._api_home_page.receive_an_employee_by_id(cookie, employee.id)
        self._api_home_page.delete_an_employee(cookie, employee_number)
        self._ui_home_page = UiHomePage(self._driver)
        self._ui_home_page.click_pim_button()
        self._ui_pim_page = UiPimPage(self._driver)
        self.assertNotIn(employee.id, self._ui_pim_page.check_employee_existence())

if __name__ == '__main__':
    unittest.main()
