from selenium.webdriver.common.by import By


# create a class for the page
class ConfirmationPage:

    # see lesson #97 - this is a constructor
    def __init__(self, driver):
        self.driver = driver

    # "button[class*='btn-success']"
    confirmCheckout = (By.CSS_SELECTOR, "button[class*='btn-success']")

    # self.driver.find_element_by_id("country").send_keys("ire")
    entersCountry = (By.ID, "country")

    # By.LINK_TEXT, "Ireland")
    displayCountry = (By.LINK_TEXT, "Ireland")
    print(displayCountry)

    # "//div[@class='checkbox checkbox-primary']"
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")

    #"//input[@type='submit']"
    confirmPurchase = (By.XPATH, "//input[@type='submit']")

    #"//div[@class='alert alert-success alert-dismissible']"
    verifyMessage = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    # creates method
    def getConfirmCheckout(self):
        return self.driver.find_element(*ConfirmationPage.confirmCheckout)

    def getCountry(self):
        return self.driver.find_element(*ConfirmationPage.entersCountry)

    def getDisplayCountry(self):
        return self.driver.find_element(*ConfirmationPage.displayCountry)

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmationPage.checkBox)

    def getConfirmPurchase(self):
        return self.driver.find_element(*ConfirmationPage.confirmPurchase)

    def getVerifyMessage(self):
        return self.driver.find_element(*ConfirmationPage.verifyMessage)
