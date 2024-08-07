import logging
import unittest
#-----------------------------INFRA CLASSES---------------------------
from orange_hrm.infra.ui.browser_wrapper import BrowserWrapper
#-----------------------------LOGIC CLASSES---------------------------
from orange_hrm.logic.config_provider import ConfigProvider
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
        self._config = ConfigProvider().load_from_file()
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
        self.assertTrue(self._home_page.check_user_details_button_displayed())

    def test_invalid_login_process(self):
        """
        This method tests invalid login flow.
        Test case: TC-02 / Invalid login.
        """
        # ACT
        self._login_page = LogInPage(self._driver)
        self._login_page.invalid_login_flow()
        # ASSERT
        self.assertEqual(self._login_page.check_invalid_login_message(), True)

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
        self.assertTrue(self._login_page.check_login_button_displayed(), True)


if __name__ == '__main__':
    unittest.main()
