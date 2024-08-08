import logging
import os
import unittest
from orange_hrm.infra.config_provider import ConfigProvider
#-----------------------------API CLASSES----------------------------
from orange_hrm.logic.api.home_page import APIHomePage
from orange_hrm.infra.api.api_wrapper import ApiWrapper
#-----------------------------UI CLASSES-----------------------------
from orange_hrm.logic.ui.log_in_page import LogInPage
from orange_hrm.logic.ui.home_page import UiHomePage
from orange_hrm.infra.ui.browser_wrapper import BrowserWrapper


class TestActiveEmployeesNumber(unittest.TestCase):

    def setUp(self):
        """
        This method initializes driver and loads config file.
        """
        logging.info("----------------Test Started----------------")
        # ARRANGE
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '../../orange_hrm.json')
        self._config = ConfigProvider().load_from_file(self._config_file_path)
        self._driver = BrowserWrapper().get_driver()
        self._api = ApiWrapper()

    def tearDown(self):
        """
        This method closes driver.
        """
        self._driver.close()
        logging.info("----------------Test Completed----------------\n")

    def test_active_employees_number(self):
        """
        This method tests active employees number.
        Test case: TC-07 / Check active employees number.
        """
        # ACT
        self._login_page = LogInPage(self._driver)
        cookie = self._login_page.valid_login_flow()
        self._api_home_page = APIHomePage(self._api)
        active_employees_number = self._api_home_page.get_active_employees_number(
                             cookie).json()['data']['numberOfActiveEmployee']
        self._ui_home_page = UiHomePage(self._driver)
        self._ui_home_page.click_about_button()
        # ASSERT
        self.assertEqual(int(self._ui_home_page.check_active_employees()),
                         active_employees_number, "Incorrect active employees number.")


if __name__ == '__main__':
    unittest.main()
