from selenium.webdriver.common.keys import Keys
from Assignment.Parameters.parameters import Parameters
from Assignment.Locators.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Humanity:

    def __init__(self, driver):
        self.driver = driver

    def LoginWithoutCredentials(self):
        self.driver.find_element_by_xpath(Locators.Log_in).click()
        element = self.driver.find_element_by_xpath(Locators.Error_message_login)
        element.is_displayed()
        self.driver.refresh()

    def LoginWithoutPassword(self, username):
        self.driver.find_element_by_css_selector(Locators.username).send_keys(username)
        self.driver.find_element_by_xpath(Locators.Log_in).click()
        element = self.driver.find_element_by_xpath(Locators.Error_message_login)
        element.is_displayed()
        self.driver.find_element_by_css_selector(Locators.username).clear()
        self.driver.refresh()

    def LoginWithoutUsername(self, password):
        self.driver.find_element_by_xpath(Locators.password).send_keys(password)
        self.driver.find_element_by_xpath(Locators.Log_in).click()
        element = self.driver.find_element_by_xpath(Locators.Error_message_login)
        element.is_displayed()
        self.driver.find_element_by_xpath(Locators.password).clear()
        self.driver.refresh()

    # def LoginWithInvalidUsername(self, username, password):
    #     self.driver.find_element_by_css_selector(Locators.username).send_keys(username)
    #     self.driver.find_element_by_xpath(Locators.password).send_keys(password)
    #     self.driver.find_element_by_xpath(Locators.Log_in).click()
    #     element = self.driver.find_element_by_xpath(Locators.Error_message_login)
    #     element.is_displayed()
    #     self.driver.refresh()

    def LoginWithInvalidPassword(self, username, password):
        self.driver.find_element_by_css_selector(Locators.username).send_keys(username)
        self.driver.find_element_by_xpath(Locators.password).send_keys(password)
        self.driver.find_element_by_xpath(Locators.Log_in).click()
        element = self.driver.find_element_by_xpath(Locators.Error_message_login)
        element.is_displayed()
        self.driver.refresh()

    def Login(self, username, password):
        self.driver.find_element_by_css_selector(Locators.username).send_keys(username)
        self.driver.find_element_by_xpath(Locators.password).send_keys(password)
        self.driver.find_element_by_xpath(Locators.Log_in).click()
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, Locators.Staff_tab)))
        element.is_displayed()
        assert self.driver.title == 'Dashboard - Dashboard - Humanity'

    def StaffTab(self):
        self.driver.find_element_by_xpath(Locators.Staff_tab).click()
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, Locators.Add_Employees)))
        element.is_displayed()
        assert self.driver.title == 'Staff - List - Humanity'

    def AddEmployeesEmptyFields(self):
        self.driver.find_element_by_xpath(Locators.Add_Employees).click()
        self.driver.find_element_by_xpath(Locators.Save_Employees).click()
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, Locators.Error_message_addEmployee)))
        element.is_displayed()
        self.driver.refresh()

    def AddEmployeesOnlyEmail(self):
        self.driver.find_element_by_css_selector(Locators.email).send_keys(Parameters.username)
        self.driver.find_element_by_xpath(Locators.Save_Employees).click()
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, Locators.Error_message_Email)))
        element.is_displayed()
        self.driver.refresh()

    def AddEmployees(self, first_name, last_name):
        self.driver.find_element_by_xpath(Locators.first_name).send_keys(first_name)
        self.driver.find_element_by_xpath(Locators.last_name).send_keys(last_name)
        self.driver.find_element_by_xpath(Locators.Save_Employees).click()
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.EmployeeAdded)))
        element.is_displayed()
        self.driver.find_element_by_xpath(Locators.All_Staff_page).click()
        assert self.driver.find_element_by_xpath(Locators.last_added_user).text == "Camilo Cienfuegos"

