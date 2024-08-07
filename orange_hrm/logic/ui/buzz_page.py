import logging
from selenium.common import TimeoutException
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from orange_hrm.infra.ui.base_page import BasePage


class UiBuzzPage(BasePage):
    """
    This class manages UI of Buzz page.
    """
    PHOTO = "div[class='orangehrm-buzz-post-body-picture']"

    def __init__(self, driver):
        super().__init__(driver)
        self._wait = WebDriverWait(self._driver, 10)

    def check_image_displayed_in_post(self):
        """
        This method checks if image is displayed in post.
        :return: bool
        """
        try:
            image = (self._wait.until
                     (EC.visibility_of_element_located
                      ((By.CSS_SELECTOR, self.PHOTO))))
            if image.is_displayed():
                return True
            else:
                return False
        except NoSuchElementException:
            logging.error("Element can not be found.")
            return False
        except TimeoutException:
            logging.error("Time out error.")
            return False
