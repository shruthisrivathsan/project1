import pytest

from Data import data
from Locators import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class Test:
    @pytest.fixture
    def boot(self):
        """ Fixture to set up and quitting the WebDriver instance."""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()

    @pytest.mark.html
    def testLogin(self,boot):
        """Set up to log into the website using the username and password"""
        self.driver.get(data.WebData().url)
        locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, "Admin")
        locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, "admin123")
        locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonLocator)
        assert self.driver.current_url == data.WebData().dashboardURL
        print("Successfully logged in")

    def testaddEmployeePim(self, boot):
        """Test case to verify adding a new employee in PIM module"""
        try:
            locator.WebLocators().selectPim(self.driver, locator.WebLocators().pimLocator) # select PIM module
            locator.WebLocators().addEmployeePim(self.driver,locator.WebLocators().addButtonLocator) # click on ADD button
            locator.WebLocators().enterEmployeeDetails(self.driver, locator.WebLocators().firstNameLocator, "Kate") # enter first name
            locator.WebLocators().enterEmployeeDetails(self.driver, locator.WebLocators().lastNameLocator, "Philip") # enter last name
            locator.WebLocators().enterEmployeeId(self.driver, locator.WebLocators().employeeIDLocator, "210") # enter employee ID
            locator.WebLocators().saveEmployeeDetails(self.driver, locator.WebLocators().saveButtonLocator) #click save to save the details
            alert = self.wait.until(EC.alert_is_present()) # wait for the alert to appear and check its text for successsful addition
            alert_text=alert.text
            assert "Success" in alert_text
            print("New employee successfully added!")
        except NoSuchElementException as e:
            print(f"Error!{e}")