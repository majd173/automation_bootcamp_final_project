import logging
import unittest
#-----------------------------API CLASSES----------------------------
from orange_hrm.logic.api.home_page import APIHomePage
from orange_hrm.infra.api.api_wrapper import ApiWrapper
from orange_hrm.infra.api.config_provider import ConfigProvider
from orange_hrm.infra.api.utilities import Utilities
from orange_hrm.logic.api.enums.preson_object import PersonObject
#-----------------------------UI CLASSES-----------------------------
from orange_hrm.logic.ui.log_in_page import LogInPage
from orange_hrm.logic.ui.home_page import UIHomePage
from orange_hrm.infra.ui.config_provider import ConfigProvider
from orange_hrm.infra.ui.browser_wrapper import BrowserWrapper


class TestOrangeHrm(unittest.TestCase):

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

    def test_changing_employee_fullname(self):
        """
        This method tests changing employee full name - UI & API.
        Test case no: 4 \
        """
        self._login_page = LogInPage(self._driver)
        cookie = self._login_page.valid_login_flow()
        self._api_home_page = APIHomePage(self._api)
        person_object = PersonObject(Utilities.generate_random_string_only_letters(5).lower(),
                                     Utilities.generate_random_string_only_letters(5).lower(),
                                     Utilities.generate_random_string_only_letters(5).lower())
        self._api_home_page.change_employee_full_name(cookie, person_object)
        home_page = UIHomePage(self._driver)
        home_page.refresh_page()
        self.assertEqual(home_page.get_admin_full_name()[0], person_object.first_name)
        self.assertEqual(home_page.get_admin_full_name()[1], person_object.last_name)


if __name__ == '__main__':
    unittest.main()
