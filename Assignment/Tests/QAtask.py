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

    def test_1_page_is_up(self):
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

    def test_2_without_credentials(self):
        H = Humanity(self.driver)
        H.LoginWithoutCredentials()

    def test_3_without_password(self):
        H = Humanity(self.driver)
        H.LoginWithoutPassword("test@test.com")

    def test_4_without_username(self):
        H = Humanity(self.driver)
        H.LoginWithoutUsername("test123!")

    # def test_5_invalid_username(self):
    #     H = Humanity(self.driver)
    #     H.LoginWithInvalidUsername("test@test123.com", Parameters.password)

    def test_5_invalid_password(self):
        H = Humanity(self.driver)
        H.LoginWithInvalidUsername(Parameters.username, "test456$")

    def test_6_login(self):
        H = Humanity(self.driver)
        H.Login(Parameters.username, Parameters.password)

    def test_7_add_employee(self):
        H = Humanity(self.driver)
        H.StaffTab()
        H.AddEmployees(Parameters.firstName, Parameters.lastName)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test is over")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner("./Reports"))
