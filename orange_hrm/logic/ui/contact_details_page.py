import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from orange_hrm.infra.ui.base_page import BasePage
from selenium.webdriver.support.expected_conditions import *


class UiContactDetailsPage(BasePage):
    """
    This class manages UI of admin contact details page.
    """
    CITY_FIELD = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input"
    MOBILE_FIELD = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input"

    def __init__(self, driver):
        super().__init__(driver)
        self._wait = WebDriverWait(self._driver, 10)

    def check_city_field_displayed(self):
        """
        This method returns the city value.
        :return: city field value.
        """
        try:
            city_field = self._wait.until(EC.visibility_of_element_located
                                          ((By.XPATH, self.CITY_FIELD)))
            if city_field.is_displayed():
                return city_field.get_attribute("value")
            else:
                return None
        except NoSuchElementException:
            logging.error("Element can not be found.")
            return None

    def check_mobile_field_displayed(self):
        """
        This method returns the mobile value.
        :return: mobile field value.
        """
        try:
            mobile_field = self._wait.until(EC.visibility_of_element_located
                                            ((By.XPATH, self.MOBILE_FIELD)))
            if mobile_field.is_displayed():
                return mobile_field.get_attribute("value")
            else:
                return None
        except NoSuchElementException:
            logging.error("Element can not be found.")
            return None
