from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()= 'Sign in']"
    expected_title = "Scouts panel - sign in"
    login_form_title_xpath = "//div/h5"
    login_form_title = "Scouts Panel"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def set_password_field(self, password):
        return self.field_send_keys(self.password_field_xpath, password)

    def click_on_sign_in_button(self):
        return self.click_on_the_element(self.sign_in_button_xpath)

    def check_login_page_title(self):
        actual_title = self.get_page_title()
        assert actual_title == self.expected_title

    def check_login_form_title(self):
        self.assert_element_text(self.login_form_title_xpath, self.login_form_title)
