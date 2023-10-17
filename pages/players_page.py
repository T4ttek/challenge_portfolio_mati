from pages.base_page import BasePage


class Players(BasePage):
    # ------------------------- Player list ----------------------------------------
    players_list = '//tbody/tr'
    name_field = '//input[@name="name"]'

    # -------------------------- Add player ----------------------------------------
    email_field = "//*[@name='email']"
    surname_field = "//input[@name='surname']"
    age_field = "//input[@name='age']"
    main_position_field = "//input[@name='mainPosition']"
    submit_button = "//button[@type='submit']"
    expected_title = "Edit player"
    edit_player_title = "//title"
    reports_link = "//ul/div[3]/div/span"

    # ------------------------- Player list ----------------------------------------

    def click_on_player(self):
        self.wait_for_element_to_be_clickable(self.players_list)
        self.click_on_the_element(self.players_list)

    # -------------------- Add player ----------------------------------------------

    def set_email_field(self, email):
        return self.field_send_keys(self.email_field, email)

    def set_name_field(self, name):
        return self.field_send_keys(self.name_field, name)

    def set_surname_field(self, surname):
        return self.field_send_keys(self.surname_field, surname)

    def set_age_field(self, age):
        return self.field_send_keys(self.age_field, age)

    def set_main_position_field(self, main_position):
        return self.field_send_keys(self.main_position_field, main_position)

    def click_on_submit_button(self):
        return self.click_on_the_element(self.submit_button)

    def check_title_starts_with(self):
        actual_title = self.get_page_title()
        assert actual_title.startswith(self.expected_title)

    def wait_for_present_of_edit_title(self):
        self.wait_for_presence_of_element_located(self.edit_player_title)

    def check_if_reports_link_is_there(self):
        self.check_if_element_is_not_present(self.reports_link)
