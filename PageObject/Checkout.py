from selenium.webdriver.common.by import By


# created class
class CheckOutPage:

    # see lesson #97
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")

    # driver.find_elements_by_xpath("//div[contains(@class, 'h-100')]")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")

    #driver.find_element_by_xpath("//a[contains(@class,'btn-primary')]")
    checkOut = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    # self.driver.find_element_by_xpath("//h4[@class='media-heading']/a")
    productSelected = (By.XPATH, "//h4[@class='media-heading']/a")


    # creates method
    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def checkOutItems(self):
        return self.driver.find_element(*CheckOutPage.checkOut)

    def getProductSelected(self):
        return self.driver.find_element(*CheckOutPage.productSelected)