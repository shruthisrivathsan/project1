from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class WebLocators:

    def __init__(self):
        """this method created to locate the different elements using name, ID, tag name, xpath and CSS-selector inorder to test OrangeHRM
        """
        self.usernameLocator = "username"
        self.passwordLocator = "password"
        self.buttonLocator = "button"
        self.pimLocator = "menu_pim_viewPimModule"
        self.addButtonLocator = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
        self.firstNameLocator = "firstName"
        self.lastNameLocator = "lastName"
        self.employeeIDLocator = "*//[@class='oxd-input oxd-input--active']"
        self.saveButtonLocator = "btnSave"
        self.employeeListLocator = "//a[@class='oxd-topbar-body-nav-tab-item' and text()='Employee List']"
        self.employeeNameLocator = "//div[@class='oxd-autocomplete-text-input oxd-autocomplete-text-input--active']"
        self.searchButtonLocator = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"
        self.editButtonLocator = "button.oxd-icon-button i.bi-pencil-fill"
        self.dropDownLocator = "oxd-select-text-input"
        self.nationalityLocator = "//div[contains(text(), 'Indian')]"
        self.saveEditButtonLocator = "//button[contains(text(), 'Save')]"
        self.deleteButtonLocator = "button.oxd-icon-button i.bi-trash"
        
    def enterText(self, driver, locator, textValue):
        """ this method is to locate the element using NAME, wait until it is located and enter the text """
        WebDriverWait(driver, 10). until(EC.presence_of_element_located((By.NAME, locator)))
        element = driver.find_element(by=By.NAME, value=locator)
        element.clear()
        element.send_keys(textValue)

    def clickButton(self, driver, locator):
        """ this method is to locate the element using TAG NAME, wait until its located and enter the text """
        driver.find_element(by=By.TAG_NAME, value=locator).click()

    def selectPim(self, driver, locator):
        """ this method is to locate the element using ID, wait until its located and enter the text """
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, locator)))
        driver.find_element(by=By.ID, value=locator).click()

    def addEmployeePim(self, driver, locator):
        """ this method is to locate the element using XPATH, wait until its located and enter the text """
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(by=By.XPATH, value=locator).click()

    def enterEmployeeDetails(self, driver, locator, textValue):
        """ this method is to locate the element using XPATH, wait until its located and enter the text """
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(by=By.NAME, value=locator).send_keys(textValue)

    def enterEmployeeId(self, driver, locator, textValue):
        """ this method is to locate the element using XPATH, wait until its located and enter the text """
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(by=By.XPATH, value=locator).send_keys(textValue)

    def saveEmployeeDetails(self, driver, locator):
        """ this method is to locate the element using NAME, wait until its located and enter the text """
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, locator)))
        driver.find_element(by=By.NAME, value=locator).click()

    def employeeList(self, driver, locator):
        """ this method is to locate the element using XPATH, wait until its located and enter the text """
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(by=By.XPATH, value=locator).click()

    def employeeNameInput(self, driver, locator, textValue):
        """ this method is to locate the element using XPATH, wait until its located and enter the text """
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(by=By.XPATH, value=locator).send_keys(textValue)

    def clickSearch(self, driver, locator):
        """ this method is to locate the element using XPATH, wait until its located and enter the text """
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(by=By.XPATH, value=locator).click()

    def clickEditButton(self, driver, locator):
        """ this method is to locate the element using CSS SELECTOR, wait until its located and enter the text """
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        driver.find_element(by=By.CSS_SELECTOR, value=locator).click()

    def clickDropDown(self, driver, locator):
        """ this method is to locate the element using CLASSNAME, wait until its located and enter the text """
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, locator)))
        driver.find_element(by=By.CLASS_NAME, value=locator).click()

    def selectNationality(self, driver, locator):
        """ this method is to locate the element using XPATH, wait until its located and enter the text """
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(by=By.XPATH, value=locator).click()

    def saveChanges(self, driver, locator):
        """ this method is to locate the element using XPATH, wait until its located and enter the text """
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,locator)))
        driver.find_element(by=By.XPATH, value=locator).click()

    def deleteEmployee(self, driver, locator):
        """ this method is to locate the element using CSS SELECTOR, wait until its located and enter the text """
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        driver.find_element(by=By.CSS_SELECTOR, value=locator).click()






