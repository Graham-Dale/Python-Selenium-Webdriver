import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
#declares fixture name
def setup(request):
    #make sure thats a lower case o in getoption
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path='C:\\Automation\Selenium\Chrome\chromedriver.exe')


    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path='C:\\Automation\Selenium\Firefox\geckodriver.exe')

    elif browser_name == "IE":
        driver = webdriver.Ie(executable_path = 'C:\\Automation\Selenium\ie\IEDriverServer.exe')

    driver.get("https://rahulshettyacademy.com/angularpractice/")

    driver.maximize_window()
    #go back and watch video that explains this #95
    request.cls.driver = driver
    yield
    driver.close()

