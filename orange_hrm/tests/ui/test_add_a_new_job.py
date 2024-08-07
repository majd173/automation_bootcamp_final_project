import logging
import unittest
# -----------------------------INFRA CLASSES----------------------------
from orange_hrm.infra.ui.browser_wrapper import BrowserWrapper
from orange_hrm.infra.utilities import Utilities
# -----------------------------LOGIC CLASSES----------------------------
from orange_hrm.logic.config_provider import ConfigProvider
from orange_hrm.logic.ui.add_save_job_page import AddSaveJobPage
from orange_hrm.logic.ui.admin_page import UiAdminPage
from orange_hrm.logic.ui.home_page import UiHomePage
from orange_hrm.logic.ui.job_categories_page import JobCategoriesPage
from orange_hrm.logic.ui.log_in_page import LogInPage


class TestAddANewJob(unittest.TestCase):

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

    def test_add_a_new_job(self):
        """
        This method tests adding a new job category.
        Test case: TC-15 / Add a new job.
        :return:
        """
        logging.info("-------------Testing Add A New Job------------")
        # ACT
        self._login_page = LogInPage(self._driver)
        self._login_page.valid_login_flow()
        self._ui_home_page = UiHomePage(self._driver)
        self._ui_home_page.click_admin_button()
        self._ui_admin_page = UiAdminPage(self._driver)
        self._ui_admin_page.click_job_button()
        self._ui_admin_page.click_job_categories_button()
        self._ui_job_categories_page = JobCategoriesPage(self._driver)
        self._ui_job_categories_page.click_add_job_button()
        self._ui_add_save_job_page = AddSaveJobPage(self._driver)
        new_job = Utilities.generate_random_string_only_letters(7)
        self._ui_add_save_job_page.insert_new_job_name(new_job)
        self._ui_add_save_job_page.click_on_save_button()
        # ASSERT
        self.assertIn(new_job, self._ui_job_categories_page.receive_job_categories_table())


if __name__ == '__main__':
    unittest.main()
