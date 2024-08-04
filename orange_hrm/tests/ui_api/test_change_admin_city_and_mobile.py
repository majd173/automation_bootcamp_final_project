import logging
import unittest
from orange_hrm.logic.api.enums.admin_contact_details import AdminContactDetails
#-----------------------------API CLASSES----------------------------
from orange_hrm.logic.api.home_page import APIHomePage
from orange_hrm.infra.api.api_wrapper import ApiWrapper
from orange_hrm.infra.api.config_provider import ConfigProvider
from orange_hrm.infra.api.utilities import Utilities
#-----------------------------UI CLASSES-----------------------------
from orange_hrm.logic.ui.log_in_page import LogInPage
from orange_hrm.logic.ui.home_page import UiHomePage
from orange_hrm.infra.ui.config_provider import ConfigProvider
from orange_hrm.infra.ui.browser_wrapper import BrowserWrapper
from orange_hrm.logic.ui.my_info_page import UiMyInfoPage
from orange_hrm.logic.ui.contact_details_page import UiContactDetailsPage


class TestAdminDetails(unittest.TestCase):


    def setUp(self):
        """
        This method initializes driver and loads config file.
        """
        logging.info("----------------Test Started----------------")
        self._config = (ConfigProvider().load_from_file
                        (r'C:\Users\Admin\Desktop\automation_bootcamp_final_project\orange_hrm\orange_hrm.json'))
        self._driver = BrowserWrapper().get_driver()
        self._api = ApiWrapper()

    def tearDown(self):
        """
        This method closes driver.
        """
        logging.info("----------------Test Completed----------------\n")
        self._driver.close()

    def test_changing_admin_city_and_mobile(self):
        self._login_page = LogInPage(self._driver)
        cookie = self._login_page.valid_login_flow()
        self._api_home_page = APIHomePage(self._api)
        admin = AdminContactDetails(
            Utilities.generate_random_string_only_letters(6),
            Utilities.generate_random_number_by_length(10))
        self._api_home_page.change_admin_city_and_mobile(cookie, admin)
        self._home_page = UiHomePage(self._driver)
        self._home_page.click_my_info_button()
        self._my_info_page = UiMyInfoPage(self._driver)
        self._my_info_page.click_contact_details_button()
        self._contact_details_page = UiContactDetailsPage(self._driver)
        self.assertEqual(self._contact_details_page.check_city_field_displayed(), admin.city)
        self.assertEqual(self._contact_details_page.check_mobile_field_displayed(), admin.mobile)



if __name__ == '__main__':
    unittest.main()
