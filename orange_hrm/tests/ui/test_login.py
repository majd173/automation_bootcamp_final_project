import logging
import os
import unittest
# -----------------------------INFRA CLASSES---------------------------
from orange_hrm.infra.ui.browser_wrapper import BrowserWrapper
# -----------------------------LOGIC CLASSES---------------------------
from orange_hrm.infra.config_provider import ConfigProvider
from orange_hrm.logic.ui.home_page import UiHomePage
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
        # ARRANGE
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '../../orange_hrm.json')
        self._config = ConfigProvider().load_from_file(self._config_file_path)
        self._driver = BrowserWrapper().get_driver()

    def tearDown(self):
        """
        This method closes driver.
        """
        self._driver.close()
        logging.info("----------------Test Completed----------------\n")

    def test_valid_login_process(self):
        """
        This method tests valid login flow.
        Test case: TC-01 / Valid login.
        """
        # ACT
        self._login_page = LogInPage(self._driver)
        self._login_page.valid_login_flow()
        self._home_page = UiHomePage(self._driver)
        # ASSERT
        self.assertTrue(self._home_page.check_user_details_button_displayed(),
                        "User details button is not displayed.")

    def test_invalid_login_process(self):
        """
        This method tests invalid login flow.
        Test case: TC-02 / Invalid login.
        """
        # ACT
        self._login_page = LogInPage(self._driver)
        self._login_page.invalid_login_flow()
        # ASSERT
        self.assertTrue(self._login_page.check_invalid_login_message(),
                        "Invalid login message is not displayed.")

    def test_logout_process(self):
        """
        This method tests logout flow.
        Test case: TC-03 / Valid logout.
        """
        # ACT
        self._login_page = LogInPage(self._driver)
        self._login_page.valid_login_flow()
        self._home_page = UiHomePage(self._driver)
        self._home_page.click_logout_button()
        # ASSERT
        self.assertTrue(self._login_page.check_login_button_displayed(),
                        "Login button is not displayed.")


if __name__ == '__main__':
    unittest.main()
