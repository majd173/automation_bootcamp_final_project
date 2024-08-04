import logging
import unittest
from orange_hrm.infra.ui.browser_wrapper import BrowserWrapper
from orange_hrm.infra.ui.config_provider import ConfigProvider
from orange_hrm.logic.ui.home_page import UIHomePage
from orange_hrm.logic.ui.log_in_page import LogInPage


class TestLogin(unittest.TestCase):
    """
    This class manages testing login and logout flow.
    """

    def setUp(self):
        """
        This method initializes driver and loads config file.
        """
        logging.info("----------------Test Started----------------")
        self._config = (ConfigProvider().load_from_file
                        (r'C:\Users\Admin\Desktop\automation_bootcamp_final_project\orange_hrm\orange_hrm.json'))
        self._driver = BrowserWrapper().get_driver()

    def tearDown(self):
        """
        This method closes driver.
        """
        logging.info("----------------Test Completed----------------\n")
        self._driver.close()

    def test_valid_login_process(self):
        """
        This method tests valid login flow.
        Test case no: 1 / Valid login.
        """
        self._login_page = LogInPage(self._driver)
        self._login_page.valid_login_flow()
        self._home_page = UIHomePage(self._driver)
        self.assertTrue(self._home_page.check_user_details_button_displayed())

    def test_invalid_login_process(self):
        """
        This method tests invalid login flow.
        Test case no: 2 / Invalid login.
        """
        self._login_page = LogInPage(self._driver)
        self._login_page.invalid_login_flow()
        self.assertEqual(self._login_page.check_invalid_login_message(), True)

    def test_logout_process(self):
        """
        This method tests logout flow.
        Test case no: 3 / Valid logout.
        """
        self._login_page = LogInPage(self._driver)
        self._login_page.valid_login_flow()
        self._home_page = UIHomePage(self._driver)
        self._home_page.click_logout_button()
        self.assertTrue(self._login_page.check_login_button_displayed(), True)


if __name__ == '__main__':
    unittest.main()
