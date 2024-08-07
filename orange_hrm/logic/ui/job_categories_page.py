import logging
from selenium.common import TimeoutException
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from orange_hrm.infra.ui.base_page import BasePage


class JobCategoriesPage(BasePage):
    """
    This class manages UI for job categories page
    """
    ADD_JOB_BUTTON = "button[class='oxd-button oxd-button--medium oxd-button--secondary']"
    JOB_CATEGORIES_TABLE = "div[row-decorator='oxd-table-decorator-card']"

    def __init__(self, driver):
        super().__init__(driver)
        self._wait = WebDriverWait(self._driver, 10)

    def click_add_job_button(self):
        """
        This method clicks on add job button.
        """
        try:
            add_job_button = (self._wait.until
                              (EC.element_to_be_clickable
                               ((By.CSS_SELECTOR, self.ADD_JOB_BUTTON))))
            add_job_button.click()
        except NoSuchElementException:
            logging.error("Element can not be found.")
        except TimeoutException:
            logging.error("Time out error.")

    def receive_job_categories_table(self):
        """
        This method returns job categories table.
        """
        try:
            job_categories_table = (self._wait.until
                                    (EC.visibility_of_element_located
                                     ((By.CSS_SELECTOR, self.JOB_CATEGORIES_TABLE))))
            if job_categories_table.is_displayed():
                return job_categories_table.text
            else:
                return None
        except NoSuchElementException:
            logging.error("Element can not be found.")
            return None
        except TimeoutException:
            logging.error("Time out error.")
            return None
