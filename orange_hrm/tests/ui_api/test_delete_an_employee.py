import logging
import os
import unittest
from orange_hrm.infra.config_provider import ConfigProvider
from orange_hrm.infra.jira_handler import JiraHandler
from orange_hrm.infra.utilities import Utilities
# -----------------------------API CLASSES----------------------------
from orange_hrm.logic.api.home_page import APIHomePage
from orange_hrm.infra.api.api_wrapper import ApiWrapper
from orange_hrm.logic.api.entities.employee_object import EmployeeObject
# -----------------------------UI CLASSES-----------------------------
from orange_hrm.logic.ui.log_in_page import LogInPage
from orange_hrm.logic.ui.home_page import UiHomePage
from orange_hrm.infra.ui.browser_wrapper import BrowserWrapper
from orange_hrm.logic.ui.pim_page import UiPimPage


class TestDeleteAnEmployee(unittest.TestCase):

    def test_delete_an_employee(self):
        """
        This method tests deleting a new employee.
        Initializing driver and api wrapper.
        Cookie is being extracted after submitting a login.
        Test case: TC-09 / Delete an employee.
        """
        logging.info("----------------Test Started----------------")
        # ARRANGE
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '../../orange_hrm.json')
        self._config = ConfigProvider().load_from_file(self._config_file_path)
        self._driver = BrowserWrapper().get_driver()
        self._api = ApiWrapper()
        self._login_page = LogInPage(self._driver)
        # ACT
        self._cookie = self._login_page.valid_login_flow()
        self._api_home_page = APIHomePage(self._api)
        employee_object = APIHomePage.generate_random_employee()
        self._api_home_page.add_a_new_employee(self._cookie, employee_object)
        employee_number = self._api_home_page.receive_an_employee_by_id(
            self._cookie, employee_object.id)
        self._api_home_page.delete_an_employee(self._cookie, employee_number)
        self._ui_home_page = UiHomePage(self._driver)
        self._ui_home_page.click_pim_button()
        self._ui_pim_page = UiPimPage(self._driver)
        # ASSERT
        try:
            self.assertNotIn(employee_object.id, self._ui_pim_page.all_employees_table(),
                             "Employee still exists.")
            self._task_flag = True
        except:
            raise

    def tearDown(self):
        """
        This method closes driver.
        Also sends a Jira issue.
        """
        if self._task_flag:
            self._jira_flag = JiraHandler()
            self._jira_flag.create_issue(
                self._config['jira_key'], 'test_delete_an_employee',
                'Add a new test that deletes all employees, use API and UI.',
                'Task')
        self._driver.close()
        logging.info("----------------Test Completed----------------\n")


if __name__ == '__main__':
    unittest.main()
