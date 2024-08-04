import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from orange_hrm.infra.ui.base_page import BasePage
from selenium.webdriver.support.expected_conditions import *



class UiMyInfoPage(BasePage):

    CONTACT_DETAILS = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a"



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


