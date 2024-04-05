#import data and locators
from Data import data
from Locators import locator
#import common
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#import explicit wait and exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class OrangeHRM:
    def __init__(self):
        """Initializes the OrangeHRM object.
            This method sets up the Chrome WebDriver and WebDriverWait objects."""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver,10)

    def boot(self):
        """Boots up the Orange HRM website.
        Navigates to the url, maximizes the window and waits for the url to match the expected url before proceeding"""
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        self.wait.until(EC.url_to_be(data.WebData().url))

    def quit(self):
        """Quits the OrangeHRM application.
            This method closes the WebDriver instance."""

        self.driver.quit()

    def login(self, username, password):
        """Logs into the OrangeHRM application.
            Args:
                username (str): The username for logging in.
                password (str): The password for logging in.

            This method navigates to the login page, enters the provided username and password,
            clicks the login button, and verifies successful login."""

        try:
            self.boot()
            locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, username)
            locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, password)
            locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonLocator)
            if self.driver.current_url == data.WebData().dashboardURL:
                print("Successfully logged in")
        except NoSuchElementException as e:
            print(f"Error! {e}")


    def addEmployeePim(self, firstname, lastname, employeeID):
        """Adds a new employee to the PIM module.
            Args:
                firstname (str): The first name of the employee.
                lastname (str): The last name of the employee.
                employeeID (str): The employee ID.
            This method navigates to the PIM module, adds a new employee by providing
            the first name, last name, and employee ID, and verifies successful addition."""

        try:
            locator.WebLocators().selectPim(self.driver, locator.WebLocators().pimLocator)
            locator.WebLocators().addEmployeePim(self.driver,locator.WebLocators().addButtonLocator)
            locator.WebLocators().enterEmployeeDetails(self.driver, locator.WebLocators().firstNameLocator, firstname)
            locator.WebLocators().enterEmployeeDetails(self.driver, locator.WebLocators().lastNameLocator, lastname)
            locator.WebLocators().enterEmployeeId(self.driver, locator.WebLocators().employeeIDLocator, employeeID)
            locator.WebLocators().saveEmployeeDetails(self.driver, locator.WebLocators().saveButtonLocator)
            alert = self.wait.until(EC.alert_is_present())
            alert_text=alert.text
            if "Success" in alert_text:
                print("New employee successfully added!")
        except NoSuchElementException as e:
            print(f"Error!{e}")

    def editEmployeePim(self, employeename):
        """Edits an existing employee in the PIM module.
            Args:
                employeename (str): The name of the employee to edit.
            This method navigates to the PIM module, searches for the specified employee,
            clicks the edit button, makes the necessary changes, and verifies successful editing."""

        try:
            locator.WebLocators().employeeList(self.driver, locator.WebLocators().employeeListLocator)
            locator.WebLocators().employeeNameInput(self.driver, locator.WebLocators().employeeNameLocator, employeename)
            locator.WebLocators().clickSearch(self.driver, locator.WebLocators().searchButtonLocator)
            locator.WebLocators().clickEditButton(self.driver, locator.WebLocators().editButtonLocator)
            locator.WebLocators().clickDropDown(self.driver, locator.WebLocators().dropDownLocator)
            locator.WebLocators().selectNationality(self.driver, locator.WebLocators().nationalityLocator)
            locator.WebLocators().saveChanges(self.driver, locator.WebLocators().saveEditButtonLocator)
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            if "Success" in alert_text:
                print("New employee successfully edited!")
        except NoSuchElementException as e:
            print(f"Error!{e}")

    def deleteEmployeePim(self, employeename):
        """Deletes an existing employee from the PIM module.
            Args:
                employeename (str): The name of the employee to delete.
            This method navigates to the PIM module, searches for the specified employee,
            clicks the delete button, confirms the deletion, and verifies successful deletion."""
        try:
            locator.WebLocators().employeeList(self.driver, locator.WebLocators().employeeListLocator)
            locator.WebLocators().employeeNameInput(self.driver, locator.WebLocators().employeeNameLocator, employeename)
            locator.WebLocators().clickSearch(self.driver, locator.WebLocators().searchButtonLocator)
            locator.WebLocators().deleteEmployee(self.driver, locator.WebLocators().deleteButtonLocator)
            self.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
            alert_text = alert.text
            if "Success" in alert_text:
                print("New employee successfully edited!")
        except NoSuchElementException as e:
            print(f"Error!{e}")


obj = OrangeHRM()
obj.login("Admin", "abc123")
obj.quit()
obj.login("Admin", "admin123")
obj.addEmployeePim("Kate", "Philip", "210")
obj.editEmployeePim("Kate Philip")
obj.deleteEmployeePim("Kate Philip")
obj.quit()