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


class TestVerifyHiringManager(unittest.TestCase):

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

    def test_verify_hiring_manager(self):
        """
        This method tests if the admin appears in the hiring managers list.
        Test case: TC-13 / Verify hiring manager.
        """
        # ACT
        self._login_page = LogInPage(self._driver)
        cookie = self._login_page.valid_login_flow()
        self._api_home_page = APIHomePage(self._api)
        self._api_home_page.get_admin_details(cookie)
        admin_firstname = self._api_home_page.get_admin_details(
            cookie).json()['data']['firstName']
        print(admin_firstname)
        # ASSERT
        self.assertIn(admin_firstname, self._api_home_page.get_hiring_manager(cookie))


if __name__ == '__main__':
    unittest.main()
