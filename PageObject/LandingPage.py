from select import select

from selenium.webdriver.common.by import By

#create a class for the page
class LandingPage:

    # see lesson #97 - this is a constructor
    def __init__(self, driver):
        self.driver = driver


    #create a variable 'shop' that represents the locator
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    checkBox = (By.ID, "exampleCheck1")
    submit = (By.XPATH, "//input[@type='submit']")
    gender = (By.ID, "exampleFormControlSelect1")
    message = (By.CLASS_NAME, "alert-success")




    #create a method that returns the locator
    def shopItems(self):
        return self.driver.find_element(*LandingPage.shop)

    def getName(self):
        return self.driver.find_element(*LandingPage.name)

    def getEmail(self):
        return self.driver.find_element(*LandingPage.email)

    def getCheckBox(self):
        return self.driver.find_element(*LandingPage.checkBox)

    def getGender(self):
        return self.driver.find_element(*LandingPage.gender)

    def getSubmit(self):
        return self.driver.find_element(*LandingPage.submit)

    def getMessage(self):
        return self.driver.find_element(*LandingPage.message)




