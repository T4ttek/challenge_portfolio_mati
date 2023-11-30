import os
import unittest
from selenium import webdriver
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

os.environ['PYTHONIOENCODING'] = 'UTF-8'


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        # os.chmod(DRIVER_PATH, 755)
        # driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome()
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        super(TestLoginPage, self).setUp(self)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.check_login_page_title()
        user_login.type_in_email("user07@getnada.com")
        user_login.set_password_field("Test-1234")
        user_login.click_on_sign_in_button()
        pass

    def test_title_of_dashboard_page(self):
        self.test_log_in_to_the_system()
        dashboard = Dashboard(self.driver)
        dashboard.check_dashboard_title()

    @classmethod
    def tearDown(self):
        self.driver.quit()
    # Element of the first task: Try to search the Internet yourself how to get rid of the error:
    # "DeprecationWarning: executable_path has been deprecated, please pass in a Service object"
