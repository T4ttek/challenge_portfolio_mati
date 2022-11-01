import os
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.players_page import Players
from pages.side_menu import SideMenu
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

os.environ['PYTHONIOENCODING'] = 'UTF-8'


class TestPlayerPage(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        os.chmod(DRIVER_PATH, 755)
        driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        dashboard = Dashboard(self.driver)
        user_login.check_login_page_title()
        user_login.type_in_email("user07@getnada.com")
        user_login.set_password_field("Test-1234")
        user_login.click_on_sign_in_button()
        dashboard.check_dashboard_title()

    def test_edit_player(self):
        side_menu = SideMenu(self.driver)
        players = Players(self.driver)
        self.test_log_in_to_the_system()
        side_menu.click_on_players_button()
        players.click_on_player()

    def test_add_player(self):
        players = Players(self.driver)
        dashboard = Dashboard(self.driver)
        self.test_log_in_to_the_system()
        players.check_if_reports_link_is_there()
        dashboard.click_on_add_player_link()
        players.set_name_field("Mateusz")
        players.set_surname_field("Greczycho")
        players.set_age_field("22051992")
        players.set_main_position_field("goalkeeper")
        players.click_on_submit_button()
        players.wait_for_present_of_edit_title()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    # Element of the first task: Try to search the Internet yourself how to get rid of the error:
    # "DeprecationWarning: executable_path has been deprecated, please pass in a Service object"
