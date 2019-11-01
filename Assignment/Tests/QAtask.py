from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Assignment.Parameters.parameters import Parameters
from Assignment.Pages.humanity import Humanity
import unittest
import HtmlTestRunner


class QaTask(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.set_page_load_timeout(10)
        cls.driver.implicitly_wait(10)
        print("Welcome to the QA task")

    def test_0_page_is_up(self):
        # if page loads within load timeout verifies title and link
        # asserts page status at the end
        pagestatus = "page loaded"
        try:
            self.driver.get(Parameters.baseURL)
            self.assertIn('Online Employee Scheduling Software | Workforce Management', self.driver.title)
            self.assertIn('https://kragujevac.humanity.com/app/', self.driver.current_url)
        except TimeoutException as ex:
            pagestatus = ex.msg
        self.assertEqual("page loaded", pagestatus)

    def test_1_without_credentials(self):
        H = Humanity(self.driver)
        H.LoginWithoutCredentials()

    def test_2_without_password(self):
        H = Humanity(self.driver)
        H.LoginWithoutPassword(Parameters.username)

    def test_3_without_username(self):
        H = Humanity(self.driver)
        H.LoginWithoutUsername(Parameters.password)

    # def test_5_invalid_username(self):
    #     H = Humanity(self.driver)
    #     H.LoginWithInvalidUsername("test@test123.com", Parameters.password)

    def test_4_invalid_password(self):
        H = Humanity(self.driver)
        H.LoginWithInvalidPassword(Parameters.username, "test456$")

    def test_5_login(self):
        H = Humanity(self.driver)
        H.Login(Parameters.username, Parameters.password)

    def test_6_add_employee_empty_fields(self):
        H = Humanity(self.driver)
        H.StaffTab()
        H.AddEmployeesEmptyFields()

    def test_7_add_employee_used_email(self):
        H = Humanity(self.driver)
        H.AddEmployeesUsedEmail()

    def test_8_add_employee_only_last_name(self):
        H = Humanity(self.driver)
        H.AddEmployeeOnlyLastName(Parameters.lastName)

    def test_9_add_employee(self):
        H = Humanity(self.driver)
        H.AddEmployees(Parameters.firstName, Parameters.lastName)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test is over")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner("./Reports"))
