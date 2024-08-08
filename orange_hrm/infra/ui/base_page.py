from orange_hrm.infra.logger_setup import LoggingSetup


class BasePage:
    """
    This class manages common functions can be used
    By any user in any type of testing project.
    """

    def __init__(self, driver):
        self._driver = driver

    # ------------------------------------------------------------------------------------------------------------

    def return_page(self):
        """
        This function refreshes the current webpage.
        """
        self._driver.refresh()

    # ------------------------------------------------------------------------------------------------------------
    def get_current_url(self):
        """
        This function returns the current website URL.
        :return: website current url
        """
        return self._driver.current_url

    # ------------------------------------------------------------------------------------------------------------
    def get_title(self):
        """
        This function returns the current website title.
        :return: website title.
        """
        return self._driver.title()
    # ------------------------------------------------------------------------------------------------------------
