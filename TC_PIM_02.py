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
    def testLogin(self, boot):
        """Set up to log into the website using the username and password"""
        self.driver.get(data.WebData().url)
        locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, "Admin")
        locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, "admin123")
        locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonLocator)
        assert self.driver.current_url == data.WebData().dashboardURL
        print("Successfully logged in")

    def testeditEmployeePim(self, boot):
        """Test case to verify editing a employee details in PIM module"""
        try:
            locator.WebLocators().employeeList(self.driver, locator.WebLocators().employeeListLocator) #select employeelist
            locator.WebLocators().employeeNameInput(self.driver, locator.WebLocators().employeeNameLocator,
                                                    "Kate Philip") #enter employee name to search for
            locator.WebLocators().clickSearch(self.driver, locator.WebLocators().searchButtonLocator) #click on search button
            locator.WebLocators().clickEditButton(self.driver, locator.WebLocators().editButtonLocator) # click on edit button
            locator.WebLocators().clickDropDown(self.driver, locator.WebLocators().dropDownLocator) # click on Nationality dropdown
            locator.WebLocators().selectNationality(self.driver, locator.WebLocators().nationalityLocator) #select Nationality
            locator.WebLocators().saveChanges(self.driver, locator.WebLocators().saveEditButtonLocator) # click on save button
            alert = self.wait.until(EC.alert_is_present()) #wait for alert to pop up and check its tect for successfull edit
            alert_text = alert.text
            assert "Success" in alert_text
            print("New employee successfully edited!")
        except NoSuchElementException as e:
            print(f"Error!{e}")