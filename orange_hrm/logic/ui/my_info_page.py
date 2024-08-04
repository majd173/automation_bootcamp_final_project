import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from orange_hrm.infra.ui.base_page import BasePage
from selenium.webdriver.support.expected_conditions import *



class UiMyInfoPage(BasePage):

    EMPLOYEE_NAME_BAR = "//p[contains(text(), 'positive man')]"



    def __init__(self, driver):
        super().__init__(driver)


    def refresh_page(self):
        time.sleep(5)
        self._driver.refresh()

    def check_employee_full_name(self):
        try:
            employee_name_bar = (WebDriverWait(self._driver, 10)
                                 .until(EC.visibility_of_element_located((By.XPATH, self.EMPLOYEE_NAME_BAR))))
            if employee_name_bar.is_displayed():
                return True
            return False
        except NoSuchElementException:
            raise NoSuchElementException("An element can not be found")