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
from orange_hrm.logic.ui.my_info_page import UiMyInfoPage


class TestChangeEmployeeGender(unittest.TestCase):

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

    def test_change_employee_gender(self):
        """
        This method tests change employee gender.
        Test case: TC-08 / Change employee's gender.
        """
        # ACT
        self._login_page = LogInPage(self._driver)
        self._cookie = self._login_page.valid_login_flow()
        self._api_home_page = APIHomePage(self._api)
        employee = PersonObject(Utilities.generate_random_string_only_letters(5),
                                Utilities.generate_random_string_only_letters(5),
                                Utilities.generate_random_string_only_letters(5))
        self._api_home_page.change_employee_gender(self._cookie, employee)
        self._ui_home_page = UiHomePage(self._driver)
        self._ui_home_page.click_my_info_button()
        self._ui_my_info_page = UiMyInfoPage(self._driver)
        # ASSERT
        self.assertTrue(self._ui_my_info_page.check_gender_button_if_enabled(employee))


if __name__ == '__main__':
    unittest.main()
