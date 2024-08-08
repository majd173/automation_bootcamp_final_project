import logging
import os
import unittest
from orange_hrm.infra.config_provider import ConfigProvider
from orange_hrm.infra.utilities import Utilities
#-----------------------------API CLASSES----------------------------
from orange_hrm.logic.api.home_page import APIHomePage
from orange_hrm.infra.api.api_wrapper import ApiWrapper
from orange_hrm.logic.api.entities.admin_contact_details import AdminContactDetails
#-----------------------------UI CLASSES-----------------------------
from orange_hrm.logic.ui.log_in_page import LogInPage
from orange_hrm.logic.ui.home_page import UiHomePage
from orange_hrm.infra.ui.browser_wrapper import BrowserWrapper
from orange_hrm.logic.ui.my_info_page import UiMyInfoPage
from orange_hrm.logic.ui.contact_details_page import UiContactDetailsPage


class TestAdminDetails(unittest.TestCase):


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

    def test_change_admin_city_and_mobile(self):
        """
        This method tests changing admin city and mobile number.
        Test case: TC-05 / Change admin's details.
        """
        # ACT
        self._login_page = LogInPage(self._driver)
        cookie = self._login_page.valid_login_flow()
        self._api_home_page = APIHomePage(self._api)
        admin = AdminContactDetails(
            Utilities.generate_random_string_only_letters(7),
            Utilities.generate_random_number_by_length(10))
        self._api_home_page.change_admin_city_and_mobile(cookie, admin)
        self._home_page = UiHomePage(self._driver)
        self._home_page.click_my_info_button()
        self._my_info_page = UiMyInfoPage(self._driver)
        self._my_info_page.click_contact_details_button()
        self._contact_details_page = UiContactDetailsPage(self._driver)
        # ASSERT
        self.assertEqual(self._contact_details_page.check_city_field_displayed(),
                         admin.city, "Updated city is not displayed.")
        self.assertEqual(self._contact_details_page.check_mobile_field_displayed(),
                         admin.mobile, "Updated mobile number is not displayed.")



if __name__ == '__main__':
    unittest.main()
