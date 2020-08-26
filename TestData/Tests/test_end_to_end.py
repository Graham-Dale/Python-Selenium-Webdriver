# allows setup (from conftest) to be mapped to this.
import pytest
import time
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# created baseeclass in utilities to get these details and not need to call setup directly.
# @pytest.mark.usefixtures("setup")
from PageObject.Checkout import CheckOutPage
from PageObject.Confirmation import ConfirmationPage
from PageObject.LandingPage import LandingPage
from Utilities.BaseClass import BaseClass

#created class for the test case, baseclass calls on setup that is in conftest.
class Test_CasesOne(BaseClass):

    def test_end_to_end(self):

        log = self.getLoggera()

        landingpage = LandingPage(self.driver)

        # clicks shop - click action i moved to the method on landing page
        landingpage.shopItems().click()

        #Start of new page (Checkout.Py)
        checkOutPage = CheckOutPage(self.driver)

        log.info("getting all the Card titles")

        # captures the products on the page
        cards = checkOutPage.getCardTitles()

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()


        # goes to checkout page
        checkOutPage.checkOutItems().click()

        # now we are on the confirmation
        # compares the name of the product from previous page to the one that is now in the cart
        # so here i captured the value of the text in his locator and called it prody.
        # and then on the next line i did the same thing but a shorter way
        prody = checkOutPage.getProductSelected().text
        assert prody == cardText
        assert cardText == checkOutPage.getProductSelected().text


        # now on confirmation page
        # actual check out confirmation
        confirmationPage = ConfirmationPage(self.driver)

        confirmationPage.getConfirmCheckout().click()

        log.info("Entering in country name")
        # enters in ire to find matching countries
        confirmationPage.getCountry().send_keys("ire")

        # puts in an explicit wait time for the list of matching Countries to come back.
        #as part of the class i was taking they told me to move this out to baseclass
        # so that it can be called by multiple test cases etc. fyi, it started off life here but
        # these guys want to modular and efficient (too much too soon)

        self.verifyLinkPresence("Ireland")

        confirmationPage.getDisplayCountry().click()

        # checks the checkbox
        confirmationPage.getCheckBox().click()

        # selects purchase
        confirmationPage.getConfirmPurchase().click()

        msg = confirmationPage.getVerifyMessage().text

        log.info(msg)

        assert " Your order will be delivered" in msg


        #self.driver.get_screenshot_as_file("screenShot.png")
