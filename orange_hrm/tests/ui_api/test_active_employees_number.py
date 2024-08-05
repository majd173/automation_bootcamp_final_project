import logging
import unittest
#-----------------------------API CLASSES----------------------------
from orange_hrm.logic.api.home_page import APIHomePage
from orange_hrm.infra.api.api_wrapper import ApiWrapper
from orange_hrm.infra.api.config_provider import ConfigProvider
#-----------------------------UI CLASSES-----------------------------
from orange_hrm.logic.ui.log_in_page import LogInPage
from orange_hrm.logic.ui.home_page import UiHomePage
from orange_hrm.infra.ui.config_provider import ConfigProvider
from orange_hrm.infra.ui.browser_wrapper import BrowserWrapper


class TestActiveEmployeesNumber(unittest.TestCase):

    def setUp(self):
        """
        This method initializes driver and loads config file.
        """
        logging.info("----------------Test Started----------------")
        # ARRANGE
        self._config = (ConfigProvider().load_from_file
                        (r'C:\Users\Admin\Desktop\automation_bootcamp_final_project\orange_hrm\orange_hrm.json'))
        self._driver = BrowserWrapper().get_driver()
        self._api = ApiWrapper()

    def tearDown(self):
        """
        This method closes driver.
        Test case: TC-07 / Check active employees number.
        """
        logging.info("----------------Test Completed----------------\n")
        self._driver.close()

    def test_active_employees_number(self):
        # ACT
        self._login_page = LogInPage(self._driver)
        cookie = self._login_page.valid_login_flow()
        self._api_home_page = APIHomePage(self._api)
        self._api_home_page.get_active_employees_number(cookie)
        active_employees_response_data = self._api_home_page.get_active_employees_number(cookie).json()
        active_employees_number = active_employees_response_data['data']['numberOfActiveEmployee']
        self._ui_home_page = UiHomePage(self._driver)
        self._ui_home_page.click_about_button()
        # ASSERT
        self.assertEqual(int(self._ui_home_page.check_active_employees()),
                         active_employees_number)


if __name__ == '__main__':
    unittest.main()
