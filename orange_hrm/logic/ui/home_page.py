import logging
from selenium.common import TimeoutException
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from orange_hrm.infra.ui.base_page import BasePage


class UiHomePage(BasePage):
    """
    This class manages UI of Home Page.
    """
    MY_INFO = "a[href='/web/index.php/pim/viewMyDetails']"
    EMPLOYEE_FULL_NAME = "//p[@class='oxd-userdropdown-name']"
    USER_DETAILS_BUTTON = "span[class='oxd-userdropdown-tab']"
    ABOUT_BUTTON = "a[href='#']"
    ACTIVE_EMPLOYEES = "//*[@id='app']/div[2]/div/div/div/div[2]/div[6]/p"
    LOGOT_BUTTON = "a[href='/web/index.php/auth/logout']"
    PIM_BUTTON = "a[href='/web/index.php/pim/viewPimModule']"
    BUZZ_BUTTON = "a[href='/web/index.php/buzz/viewBuzz']"
    ADMIN_BUTTON = "a[href='/web/index.php/admin/viewAdminModule']"

    def __init__(self, driver):
        super().__init__(driver)
        self._wait = WebDriverWait(self._driver, 10)

    def get_admin_full_name(self):
        """
        This method gets admin full name.
        :return: admin full name.
        """
        try:
            admin_full_name = (self._wait.until
                               (EC.visibility_of_element_located
                                ((By.XPATH, self.EMPLOYEE_FULL_NAME))))
            return admin_full_name.text.split(" ")
        except NoSuchElementException:
            logging.error("Element can not be found.")
            return None
        except TimeoutException:
            logging.error("Time out error.")
            return None

    def refresh_page(self):
        """
        This method refreshes page.
        """
        try:
            self._driver.refresh()
        except Exception as e:
            logging.error(f'Can not refresh page. {e}')

    def click_user_details_button(self):
        """
        This method clicks on user details button.
        """
        try:
            user_details_button = (self._wait.until
                                   (EC.element_to_be_clickable
                                    ((By.CSS_SELECTOR, self.USER_DETAILS_BUTTON))))
            user_details_button.click()
        except NoSuchElementException:
            logging.error("Element can not be found.")
        except TimeoutException:
            logging.error("Time out error.")

    def click_logout_button(self):
        """
        This method clicks on logout button.
        """
        try:
            self.click_user_details_button()
            logout_button = (self._wait.until
                             (EC.element_to_be_clickable
                              ((By.CSS_SELECTOR, self.LOGOT_BUTTON))))
            logout_button.click()
        except NoSuchElementException:
            logging.error("Element can not be found.")
        except TimeoutException:
            logging.error("Time out error.")

    def check_user_details_button_displayed(self):
        """
        This method checks if user details button is displayed.
        """
        try:
            user_details_button = (self._wait.until
                                   (EC.element_to_be_clickable
                                    ((By.CSS_SELECTOR, self.USER_DETAILS_BUTTON))))
            if user_details_button.is_displayed():
                return True
            else:
                return False
        except NoSuchElementException:
            logging.error("Element can not be found.")
            return False
        except TimeoutException:
            logging.error("Time out error.")
            return False

    def click_my_info_button(self):
        """
        This method clicks on my info button.
        """
        try:
            my_info_button = (self._wait.until
                              (EC.element_to_be_clickable
                               ((By.CSS_SELECTOR, self.MY_INFO))))
            my_info_button.click()
        except NoSuchElementException:
            logging.error("Element can not be found.")
        except TimeoutException:
            logging.error("Time out error.")

    def click_pim_button(self):  # pim = personal information management
        """
        This method clicks on pim (personal information management) button.
        """
        try:
            pim_button = (self._wait.until
                          (EC.element_to_be_clickable
                           ((By.CSS_SELECTOR, self.PIM_BUTTON))))
            pim_button.click()
        except NoSuchElementException:
            logging.error("Element can not be found.")
        except TimeoutException:
            logging.error("Time out error.")

    def click_about_button(self):
        """
        This method clicks on about button.
        :return:
        """
        self.click_user_details_button()
        try:
            about_button = (self._wait.until
                            (EC.element_to_be_clickable
                             ((By.CSS_SELECTOR, self.ABOUT_BUTTON))))
            about_button.click()
        except NoSuchElementException:
            logging.error("Element can not be found.")
        except TimeoutException:
            logging.error("Time out error.")

    def check_active_employees(self):
        """
        This method returns number of active employees.
        :return: active employees number.
        """
        try:
            active_employees = (self._wait.until
                                (EC.visibility_of_element_located
                                 ((By.XPATH, self.ACTIVE_EMPLOYEES))))
            if active_employees.is_displayed():
                return active_employees.text
            else:
                return None
        except NoSuchElementException:
            logging.error("Element can not be found.")
            return None
        except TimeoutException:
            logging.error("Time out error.")
            return None

    def click_buzz_button(self):
        """
        This method clicks on buzz button.
        """
        try:
            buzz_button = (self._wait.until
                           (EC.element_to_be_clickable
                            ((By.CSS_SELECTOR, self.BUZZ_BUTTON))))
            buzz_button.click()
        except NoSuchElementException:
            logging.error("Element can not be found.")
        except TimeoutException:
            logging.error("Time out error.")

    def click_admin_button(self):
        """
        This method clicks on admin button.
        """
        try:
            admin_button = (self._wait.until
                            (EC.element_to_be_clickable
                             ((By.CSS_SELECTOR, self.ADMIN_BUTTON))))
            admin_button.click()
            logging.info("Clicking on admin button.")
        except NoSuchElementException:
            logging.error("Element can not be found.")
        except TimeoutException:
            logging.error("Time out error.")
