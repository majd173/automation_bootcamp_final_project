import logging
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from orange_hrm.infra.ui.base_page import BasePage


class UiHomePage(BasePage):
    MY_INFO = "a[href='/web/index.php/pim/viewMyDetails']"
    EMPLOYEE_FULL_NAME = "//p[@class='oxd-userdropdown-name']"
    USER_DETAILS_BUTTON = "span[class='oxd-userdropdown-tab']"
    ABOUT_BUTTON = "a[href='#']"
    ACTIVE_EMPLOYEES = "//*[@id='app']/div[2]/div/div/div/div[2]/div[6]/p"
    LOGOT_BUTTON = "a[href='/web/index.php/auth/logout']"
    PIM_BUTTON = "a[href='/web/index.php/pim/viewPimModule']"


    def __init__(self, driver):
        super().__init__(driver)
        self._wait = WebDriverWait(self._driver, 10)

    def get_admin_full_name(self):
        employee_full_name = self._wait.until(EC.visibility_of_element_located
                                              ((By.XPATH, self.EMPLOYEE_FULL_NAME)))
        return employee_full_name.text.split(" ")

    def refresh_page(self):
        self._driver.refresh()

    def click_user_details_button(self):
        try:
            user_details_button = self._wait.until(EC.element_to_be_clickable
                                                   ((By.CSS_SELECTOR, self.USER_DETAILS_BUTTON)))
            user_details_button.click()
        except NoSuchElementException:
            logging.error("Element can not be found.")

    def click_logout_button(self):
        try:
            self.click_user_details_button()
            logout_button = self._wait.until(EC.element_to_be_clickable
                                             ((By.CSS_SELECTOR, self.LOGOT_BUTTON)))
            logout_button.click()
        except NoSuchElementException:
            logging.error("Element can not be found.")

    def check_user_details_button_displayed(self):
        try:
            user_details_button = self._wait.until(EC.element_to_be_clickable
                                                   ((By.CSS_SELECTOR, self.USER_DETAILS_BUTTON)))
            if user_details_button.is_displayed():
                return True
            else:
                return False
        except NoSuchElementException:
            logging.error("Element can not be found.")

    def click_my_info_button(self):
        try:
            my_info_button = self._wait.until(EC.element_to_be_clickable
                                              ((By.CSS_SELECTOR, self.MY_INFO)))
            my_info_button.click()
        except NoSuchElementException:
            logging.error("Element can not be found.")

    def click_pim_button(self):
        try:
            pim_button = self._wait.until(EC.element_to_be_clickable
                                          ((By.CSS_SELECTOR, self.PIM_BUTTON)))
            pim_button.click()
        except NoSuchElementException:
            logging.error("Element can not be found.")

    def click_about_button(self):
        self.click_user_details_button()
        about_button = (self._wait.until
                        (EC.element_to_be_clickable
                         ((By.CSS_SELECTOR, self.ABOUT_BUTTON))))
        about_button.click()


