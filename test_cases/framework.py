import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

os.environ['PYTHONIOENCODING'] = 'UTF-8'


class Test(unittest.TestCase):

    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def tearDown(self):
        self.driver.quit()

    def test_print_nice_words(self):
        print("WELL DONE!!!!!!!!!")

    # Element of the first task: Try to search the Internet yourself how to get rid of the error:
    # "DeprecationWarning: executable_path has been deprecated, please pass in a Service object"
