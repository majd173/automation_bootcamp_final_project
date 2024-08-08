import logging
import os
import unittest
from orange_hrm.infra.config_provider import ConfigProvider
from orange_hrm.infra.utilities import Utilities
# -----------------------------API CLASSES----------------------------
from orange_hrm.logic.api.home_page import APIHomePage
from orange_hrm.infra.api.api_wrapper import ApiWrapper
# -----------------------------UI CLASSES-----------------------------
from orange_hrm.logic.ui.log_in_page import LogInPage
from orange_hrm.infra.ui.browser_wrapper import BrowserWrapper


class TestDeleteNonExistentEmployee(unittest.TestCase):

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

    def test_non_existent_employee(self):
        """
        This method tests deleting a non-existent employee.
        Test case: TC-14 / Delete a non-existent employee.
        """
        # ACT
        self._login_page = LogInPage(self._driver)
        cookie = self._login_page.valid_login_flow()
        self._api_home_page = APIHomePage(self._api)
        non_existent_employee = self._api_home_page.delete_an_employee(
            cookie, Utilities.generate_random_number_by_length(4))
        # ASSERT
        self.assertFalse(non_existent_employee.ok, "Request has been accepted.")
        self.assertEqual(non_existent_employee.status_code, 404, "Status code is not 404.")


if __name__ == '__main__':
    unittest.main()
