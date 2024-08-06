import logging
import unittest
from orange_hrm.logic.config_provider import ConfigProvider
#-----------------------------API CLASSES----------------------------
from orange_hrm.logic.api.home_page import APIHomePage
from orange_hrm.infra.api.api_wrapper import ApiWrapper
from orange_hrm.logic.ui.buzz_page import UiBuzzPage
#-----------------------------UI CLASSES-----------------------------
from orange_hrm.logic.ui.log_in_page import LogInPage
from orange_hrm.logic.ui.home_page import UiHomePage
from orange_hrm.infra.ui.browser_wrapper import BrowserWrapper


class TestSharePhoto(unittest.TestCase):

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

    def test_share_a_photo_by_post(self):
        """
        This method tests sharing a photo by post.
        Test case: TC-12 / Share a photo by a post.
        """
        # ACT
        self._login_page = LogInPage(self._driver)
        cookie = self._login_page.valid_login_flow()
        self._api_home_page = APIHomePage(self._api)
        self._api_home_page.share_a_photo_by_post(cookie, self._config['share_photo'])
        self._ui_home_page = UiHomePage(self._driver)
        self._ui_home_page.click_buzz_button()
        self._ui_buzz_page = UiBuzzPage(self._driver)
        # ASSERT
        self.assertTrue(self._ui_buzz_page.check_image_displayed_in_post(),
                        "Photo is not displayed (has not been shared).")


if __name__ == '__main__':
    unittest.main()
