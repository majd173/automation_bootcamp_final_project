import logging
from selenium.common import TimeoutException
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from orange_hrm.infra.ui.base_page import BasePage


class UiAdminPage(BasePage):
    """
    This class manages UI for admin page.
    """
    JOB_BUTTON = "//span[contains(text(),'Job')]"
    JOB_CATEGORIES_BUTTON = "//a[contains(text(),'Job Categories')]"

    def __init__(self, driver):
        super().__init__(driver)
        self._wait = WebDriverWait(self._driver, 10)

    def click_job_button(self):
        """
        This method clicks on job button.
        """
        try:
            job_button = (self._wait.until
                          (EC.element_to_be_clickable
                           ((By.XPATH, self.JOB_BUTTON))))
            job_button.click()
        except NoSuchElementException:
            logging.error("Element can not be found.")
        except TimeoutException:
            logging.error("Time out error.")

    def click_job_categories_button(self):
        """
        This method clicks on job categories button.
        """
        try:
            job_categories_button = (self._wait.until
                                     (EC.element_to_be_clickable
                                      ((By.XPATH, self.JOB_CATEGORIES_BUTTON))))
            job_categories_button.click()
        except NoSuchElementException:
            logging.error("Element can not be found.")
        except TimeoutException:
            logging.error("Time out error.")
