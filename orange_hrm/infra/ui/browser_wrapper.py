import logging
import os
from selenium import webdriver
from orange_hrm.infra.config_provider import ConfigProvider


class BrowserWrapper:
    """
    This class manages choosing a browser.
    """

    def __init__(self):
        self._driver = None  # because I still don't know which driver to choose.
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '../../orange_hrm.json')
        self.config = ConfigProvider.load_from_file(self._config_file_path)

    def get_driver(self):
        """
        This method determines which browser to open and also opens it.
        :return: self._driver
        """
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
            logging.error("Browser not found.")

        self._driver.get(url)
        self._driver.maximize_window()
        return self._driver


