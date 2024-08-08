import logging
import os
import unittest
from orange_hrm.infra.config_provider import ConfigProvider
from orange_hrm.infra.utilities import Utilities
#-----------------------------API CLASSES----------------------------
from orange_hrm.logic.api.home_page import APIHomePage
from orange_hrm.infra.api.api_wrapper import ApiWrapper
from orange_hrm.logic.api.entities.admin_object import AdminObject
#-----------------------------UI CLASSES-----------------------------
from orange_hrm.logic.ui.log_in_page import LogInPage
from orange_hrm.logic.ui.home_page import UiHomePage
from orange_hrm.infra.ui.browser_wrapper import BrowserWrapper
from orange_hrm.logic.ui.my_info_page import UiMyInfoPage


class TestChangeAdminGender(unittest.TestCase):

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

    def test_change_employee_gender(self):
        """
        This method tests change admin gender.
        Test case: TC-08 / Change employee's gender.
        """
        # ACT
        self._login_page = LogInPage(self._driver)
        self._cookie = self._login_page.valid_login_flow()
        self._api_home_page = APIHomePage(self._api)
        admin_object = AdminObject(Utilities.generate_random_string_only_letters(5),
                                   Utilities.generate_random_string_only_letters(5),
                                   Utilities.generate_random_string_only_letters(5))
        self._api_home_page.change_admin_gender(self._cookie, admin_object)
        self._ui_home_page = UiHomePage(self._driver)
        self._ui_home_page.click_my_info_button()
        self._ui_my_info_page = UiMyInfoPage(self._driver)
        # ASSERT
        self.assertTrue(self._ui_my_info_page.check_gender_button_if_enabled(admin_object),
                        "Gender button is not enabled.")


if __name__ == '__main__':
    unittest.main()
