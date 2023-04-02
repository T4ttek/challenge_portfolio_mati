from pages.base_page import BasePage


class Dashboard(BasePage):
    expect_title = "Scouts panel"
    add_player_link = '//h2/following-sibling::a/button'
    add = "(//a/descendant::span)[3]"
    players_count = "//main/div[2]/div[1]//b"

    def check_dashboard_title(self):
        self.wait_for_presence_of_element_located(self.add_player_link)
        assert self.get_page_title() == self.expect_title

    def click_on_add_player_link(self):
        return self.click_on_the_element(self.add)
