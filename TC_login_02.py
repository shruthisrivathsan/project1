import pytest

from Data import data
from Locators import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class Test:
    @pytest.fixture
    def boot(self):
        """ Fixture to set up and quitting the WebDriver instance."""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.quit()

    @pytest.mark.html
    def testLoginIncorrectCred(self,boot):
        """Test case to verify login functionality. """
        self.driver.get(data.WebData().url)
        locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, "Admin")
        locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, "administrator")
        locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonLocator)
        assert "dashboard" not in self.driver.current_url
        print("Incorrect credentials")

