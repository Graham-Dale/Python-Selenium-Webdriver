import inspect
import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    # creates method
    def verifyLinkPresence(self, text):
        # come back to this one and see how to capture this via the page object mechanism
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    # currently using this one for the gender dropdown.
    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def getLoggera(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('C:\\Users\\Home Laptop\\PycharmProjects\\pythonSelFramework\\Tests\\logfilea.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # A file handler object

        logger.setLevel(logging.DEBUG)  # For some reason it needs the level in uppercase. Need to figure that out.

        return logger
