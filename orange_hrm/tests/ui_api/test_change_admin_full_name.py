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


class TestChangeAdminFullName(unittest.TestCase):

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

    def test_change_admin_fullname(self):
        """
        This method tests changing admin full name - UI & API.
        Test case: TC-04 / Change admin full name.
        """
        # ACT
        self._login_page = LogInPage(self._driver)
        cookie = self._login_page.valid_login_flow()
        self._api_home_page = APIHomePage(self._api)
        admin_object = AdminObject(Utilities.generate_random_string_only_letters(5).lower(),
                                   Utilities.generate_random_string_only_letters(5).lower(),
                                   Utilities.generate_random_string_only_letters(5).lower())
        self._api_home_page.change_admin_full_name(cookie, admin_object)
        home_page = UiHomePage(self._driver)
        home_page.refresh_page()
        # ASSERT
        self.assertEqual(home_page.get_admin_full_name()[0], admin_object.first_name)
        self.assertEqual(home_page.get_admin_full_name()[1], admin_object.last_name)


if __name__ == '__main__':
    unittest.main()
