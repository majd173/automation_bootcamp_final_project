import logging
from selenium import webdriver
from orange_hrm.infra.api.config_provider import ConfigProvider


class BrowserWrapper:
    # This class manages choosing a browser.
    def __init__(self):
        self._driver = None # because I still don't know which driver to choose.
        self.config = ConfigProvider.load_from_file(r'C:\Users\Admin\Desktop\Automation_bootcamp\orange_hrm\orange_hrm.json')
    # ------------------------------------------------------------------------------------------------------------
    # This function determines which browser to open and also opens it.
    def get_driver(self):
        url = self.config.get("login_url")
        if not url:
            raise ValueError("URL not found in the configuration.")
        if self.config["browser"] == "Chrome":
            self._driver = webdriver.Chrome()
        elif self.config["browser"] == "FireFox":
            self._driver = webdriver.Firefox()
        elif self.config["browser"] == "Edge":
            self._driver = webdriver.Edge()
        else:
            logging.error("")

        self._driver.get(url)
        self._driver.maximize_window()
        return self._driver
