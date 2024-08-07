import logging
from selenium.common import TimeoutException
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from orange_hrm.infra.ui.base_page import BasePage
from orange_hrm.logic.config_provider import ConfigProvider
from orange_hrm.infra.utilities import Utilities


class LogInPage(BasePage):
    """
    This class manages UI for login page and login flow.
    """
    USERNAME_INPUT = "input[name='username']"
    PASSWORD_INPUT = "input[type='password']"
    LOGIN_BUTTON = "button[type='submit']"
    INVALID_LOGIN_MESSAGE = "div[class='oxd-alert-content oxd-alert-content--error']"

    def __init__(self, driver):
        super().__init__(driver)
        self._config = ConfigProvider().load_from_file()
        self._wait = WebDriverWait(self._driver, 10)

    def insert_username(self):
        """
        This method inserts valid username from config file.
        """
        try:
            username_input = (self._wait.until
                              (EC.element_to_be_clickable
                               ((By.CSS_SELECTOR, self.USERNAME_INPUT))))
            username_input.send_keys(self._config["username"])
        except NoSuchElementException:
            logging.error("Element can not be found.")
        except TimeoutException:
            logging.error("Time out error.")

    def insert_password(self):
        """
        This method inserts valid password from config file.
        """
        try:
            password_input = (self._wait.until
                              (EC.element_to_be_clickable
                               ((By.CSS_SELECTOR, self.PASSWORD_INPUT))))
            password_input.send_keys(self._config["password"])
        except NoSuchElementException:
            logging.error("Element can not be found.")
        except TimeoutException:
            logging.error("Time out error.")

    def insert_generated_username(self):
        """
        This method inserts invalid generated username.
        """
        try:
            username_input = (self._wait.until
                              (EC.element_to_be_clickable
                               ((By.CSS_SELECTOR, self.USERNAME_INPUT))))
            username_input.send_keys(Utilities.generate_random_string_only_letters(7))
        except NoSuchElementException:
            logging.error("Element can not be found.")
        except TimeoutException:
            logging.error("Time out error.")

    def insert_generated_password(self):
        """
        This method inserts invalid generated password.
        """
        try:
            password_input = (self._wait.until
                              (EC.element_to_be_clickable
                               ((By.CSS_SELECTOR, self.PASSWORD_INPUT))))
            password_input.send_keys(Utilities.generate_random_string_with_punctuation(7))
        except NoSuchElementException:
            logging.error("Element can not be found.")
        except TimeoutException:
            logging.error("Time out error.")

    def click_log_in_button(self):
        """
        This method clicks on login button.
        """
        try:
            login_button = (self._wait.until
                            (EC.element_to_be_clickable
                             ((By.CSS_SELECTOR, self.LOGIN_BUTTON))))
            login_button.click()
        except NoSuchElementException:
            logging.error("Element can not be found.")
        except TimeoutException:
            logging.error("Time out error.")

    def valid_login_flow(self):
        """
        This method performs valid login flow.
        :return: website cookies.
        """
        try:
            logging.info("Trying a valid logging in flow process.")
            self.insert_username()
            self.insert_password()
            self.click_log_in_button()
            cookies = self._driver.get_cookies()
            if cookies:
                return {
                    "Cookie": f'orangehrm={cookies[0]['value']}'
                }
            else:
                logging.error("Cookies can not be found.")
        except Exception as e:
            logging.error(f'Valid login process failed: {e}')


    def invalid_login_flow(self):
        """
        This method performs invalid login flow.
        """
        try:
            logging.info("Trying an invalid logging in flow process.")
            self.insert_generated_username()
            self.insert_generated_password()
            self.click_log_in_button()
        except Exception as e:
            logging.error(f'Invalid login process failed: {e}')

    def check_invalid_login_message(self):
        """
        This method checks if invalid login message is displayed.
        :return: boolean
        """
        try:
            invalid_login_message = (self._wait.until
                                     (EC.presence_of_element_located
                                      ((By.CSS_SELECTOR, self.INVALID_LOGIN_MESSAGE))))
            if invalid_login_message.is_displayed():
                logging.info("Invalid login message is displayed.")
                return True
            else:
                logging.error("Invalid login message is not displayed.")
                return False
        except NoSuchElementException:
            logging.error("Element can not be found.")
            return False
        except TimeoutException:
            logging.error("Time out error.")
            return False

    def check_login_button_displayed(self):
        """
        This method checks if login button is displayed.
        :return: boolean
        """
        try:
            logging.info("Trying valid logging out flow process,"
                         " by checking visibility of login button after submitting a logout.")
            login_button = (self._wait.until
                            (EC.element_to_be_clickable
                             ((By.CSS_SELECTOR, self.LOGIN_BUTTON))))
            if login_button.is_displayed():
                logging.info("Login button is displayed.")
                return True
            else:
                logging.error("Login button is not displayed.")
                return False
        except NoSuchElementException:
            logging.error("Element can not be found.")
            return False
        except TimeoutException:
            logging.error("Time out error.")
            return False
