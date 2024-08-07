import logging
import unittest
from orange_hrm.infra.utilities import Utilities
from orange_hrm.logic.config_provider import ConfigProvider
#-----------------------------API CLASSES----------------------------
from orange_hrm.logic.api.home_page import APIHomePage
from orange_hrm.infra.api.api_wrapper import ApiWrapper
#-----------------------------UI CLASSES-----------------------------
from orange_hrm.logic.ui.log_in_page import LogInPage
from orange_hrm.infra.ui.browser_wrapper import BrowserWrapper


class TestAddANewPost(unittest.TestCase):

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

    def test_add_a_new_post(self):
        """
        This method tests adding a new post.
        Test case: TC-10 / Add a new post.
        """
        # ACT
        self._login_page = LogInPage(self._driver)
        cookie = self._login_page.valid_login_flow()
        generated_post = Utilities.generate_random_string_with_punctuation(20)
        self._api_home_page = APIHomePage(self._api)
        post_request = self._api_home_page.add_a_new_post(cookie, generated_post)
        # ASSERT
        self.assertTrue(post_request.ok,
                        "Post has not benn accepted.")
        self.assertEqual(post_request.status_code,
                         200, "Status code is not 200.")


if __name__ == '__main__':
    unittest.main()
