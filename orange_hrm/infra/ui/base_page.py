from orange_hrm.infra.ui.logger_setup import LoggingSetup
class BasePage:
    # This class manages common functions can be used
    #by any user in any type of testing project.

    def __init__(self, driver):
        self._driver = driver
    # ------------------------------------------------------------------------------------------------------------
    # This function refreshes the current webpage.
    def return_page(self):
        self._driver.refresh()
    # ------------------------------------------------------------------------------------------------------------
    # This function returns the current website URL.
    def get_current_url(self):
        return self._driver.current_url
    # ------------------------------------------------------------------------------------------------------------
    # This function returns the current website title.
    def get_title(self):
        return self._driver.title()
    # ------------------------------------------------------------------------------------------------------------
