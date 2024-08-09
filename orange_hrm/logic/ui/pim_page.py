import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from orange_hrm.infra.ui.base_page import BasePage
from selenium.webdriver.support.expected_conditions import *


class UiPimPage(BasePage):
    """
    This class manages UI for PIM page (personal information management).
    """
    EMPLOYEES_TABLE = "div[class='oxd-table-body']"

    def __init__(self, driver):
        super().__init__(driver)
        self._wait = WebDriverWait(self._driver, 10)

    def all_employees_table(self):
        """
        This method receives table of all employees.
        :return: extracted text from employees table.
        """
        try:
            logging.info("Receiving table of all employees.")
            employees_table = (self._wait.until
                               (EC.visibility_of_element_located
                                ((By.CSS_SELECTOR, self.EMPLOYEES_TABLE))))
            if employees_table.is_displayed():
                return employees_table.text
            else:
                return None
        except NoSuchElementException:
            logging.error("Element can not be found.")
            return None

