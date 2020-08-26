import pytest
from selenium.webdriver.support.select import Select

from selenium import webdriver

from PageObject.LandingPage import LandingPage
from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass

class Test_HomePage(BaseClass):

    def test_formSubmission(self, getData):
        landingPage = LandingPage(self.driver)

        # Name
        landingPage.getName().send_keys(getData["firstname"])

        # eMail
        landingPage.getEmail().send_keys(getData["email"])

        # Gender - dropdown
        # Note, the logic has bene placed ino the base class as selectoptionbytext for re-use
        # So, we call on that and then steer it to capture the value in the landing page
        # Finally, the value of Female is chosen by text

        self.selectOptionByText(landingPage.getGender(), getData["gender"])

        # used to be
        # sel = Select(landingPage.gotGender())
        # sel.select_by_visible_text("Male")

        landingPage.getSubmit().click()

        self.driver.implicitly_wait(10)

        msg = landingPage.getMessage().text
        # message = self.driver.find_element_by_class_name("alert-success").text

        #Am leaving this here as its handy for running in the console
        print(msg)


        assert "success" in msg

        self.driver.refresh()

    # This is a fixture
    # added  tuples to the following
    #Originally was taking data from this file but now using a data file. Leaving this there in case i want to flip to local
    # @pytest.fixture(params=[("graham dale", "graham_dale@yahoo.com","Male"),("Balto","irish0341@gmail.com","Female")])
    # def getData(self, request):
    #    return request.param

    @pytest.fixture(params=HomePageData.getTestData("T6"))
    def getData(self, request):
        return request.param