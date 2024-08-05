import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from orange_hrm.infra.ui.base_page import BasePage
from selenium.webdriver.support.expected_conditions import *


class UiMyInfoPage(BasePage):
    CONTACT_DETAILS = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a"
    FEMALE_RADIO_BUTTON = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label/span"

    def __init__(self, driver):
        super().__init__(driver)
        self._wait = WebDriverWait(self._driver, 10)

    def click_contact_details_button(self):
        try:
            contact_details_button = self._wait.until(EC.element_to_be_clickable
                                                      ((By.XPATH, self.CONTACT_DETAILS)))
            contact_details_button.click()
        except NoSuchElementException:
            logging.error("Element can not be found.")

    def check_female_button_clickable(self):
        try:
            female_button = self._wait.until(EC.element_to_be_clickable
                                             ((By.XPATH, self.FEMALE_RADIO_BUTTON)))
            if female_button.is_enabled():
                return True
            else:
                return False
        except NoSuchElementException:
            logging.error("Element can not be found.")
