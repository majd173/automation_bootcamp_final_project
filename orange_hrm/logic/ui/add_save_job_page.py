import logging
from selenium.common import TimeoutException
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from orange_hrm.infra.ui.base_page import BasePage


class AddSaveJobPage(BasePage):
    """This class manages UI for add new job page and save flow."""
    JOB_INPUT = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input"
    SAVE_JOB_BUTTON = "button[class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"

    def __init__(self, driver):
        super().__init__(driver)
        self._wait = WebDriverWait(self._driver, 10)

    def insert_new_job_name(self, job_name):
        """
        This method inserts new job name.
        :param job_name: new job name
        """
        try:
            new_job_name = (self._wait.until
                            (EC.element_to_be_clickable
                             ((By.XPATH, self.JOB_INPUT))))
            new_job_name.send_keys(job_name)
            logging.info("Inserting new job name.")
        except NoSuchElementException:
            logging.error("Element can not be found.")
        except TimeoutException:
            logging.error("Time out error.")

    def click_on_save_button(self):
        """
        This method clicks on save button.
        """
        try:
            save_button = (self._wait.until
                           (EC.element_to_be_clickable
                            ((By.CSS_SELECTOR, self.SAVE_JOB_BUTTON))))
            save_button.click()
            logging.info("Clicking on save button.")
        except NoSuchElementException:
            logging.error("Element can not be found.")
        except TimeoutException:
            logging.error("Time out error.")
