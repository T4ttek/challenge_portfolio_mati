import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class Test(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        # driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome()
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_print_nice_words(self):
        print("WELL DONE !!!!!!!!!!!!!!")