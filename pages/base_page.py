import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from utils.settings import DEFAULT_LOCATOR_TYPE


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def field_send_keys(self, selector, value, locator_type=DEFAULT_LOCATOR_TYPE):
        return self.driver.find_element(locator_type, selector).send_keys(value)

    def click_on_the_element(self, selector, selector_type=DEFAULT_LOCATOR_TYPE):
        return self.driver.find_element(selector_type, selector).click()

    def get_page_title(self):
        return self.driver.title

    def assert_element_text(self, xpath, expected_text):
        """Comparing expected text with observed value from web element
            :param xpath: xpath to element with text to be observed
            :param expected_text: text what we're expecting to be found
            :return: None
        """
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        element_text = element.text
        assert expected_text == element_text

    def wait_for_element_to_be_clickable(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((locator_type, locator)))
        return element

    def wait_for_presence_of_element_located(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        element = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((locator_type, locator)))
        return element

    def check_if_element_is_not_present(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        element = WebDriverWait(self.driver, 10).until(ec.invisibility_of_element_located((locator_type, locator)))
