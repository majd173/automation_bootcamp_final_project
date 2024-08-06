import logging
import unittest
from orange_hrm.logic.config_provider import ConfigProvider
#-----------------------------API CLASSES----------------------------
from orange_hrm.logic.api.home_page import APIHomePage
from orange_hrm.infra.api.api_wrapper import ApiWrapper
from orange_hrm.infra.utilities import Utilities
from orange_hrm.logic.api.entities.preson_object import PersonObject
#-----------------------------UI CLASSES-----------------------------
from orange_hrm.logic.ui.log_in_page import LogInPage
from orange_hrm.logic.ui.home_page import UiHomePage
from orange_hrm.infra.ui.browser_wrapper import BrowserWrapper


class TestChangingEmployeeFullName(unittest.TestCase):

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


    def test_change_employee_fullname(self):
        """
        This method tests changing employee full name - UI & API.
        Test case: TC-04 / Change employee full name.
        """
        # ACT
        self._login_page = LogInPage(self._driver)
        cookie = self._login_page.valid_login_flow()
        self._api_home_page = APIHomePage(self._api)
        person_object = PersonObject(Utilities.generate_random_string_only_letters(5).lower(),
                                     Utilities.generate_random_string_only_letters(5).lower(),
                                     Utilities.generate_random_string_only_letters(5).lower(),
                                     1)
        self._api_home_page.change_employee_full_name(cookie, person_object)
        home_page = UiHomePage(self._driver)
        home_page.refresh_page()
        # ASSERT
        self.assertEqual(home_page.get_admin_full_name()[0], person_object.first_name)
        self.assertEqual(home_page.get_admin_full_name()[1], person_object.last_name)


if __name__ == '__main__':
    unittest.main()
