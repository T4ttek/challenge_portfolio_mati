from pages.base_page import BasePage


class SideMenu(BasePage):

    players_button = '//div/ul[1]/div[2]'

    def click_on_players_button(self):
        self.click_on_the_element(self.players_button)
