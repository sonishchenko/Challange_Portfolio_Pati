from pages.base_page import BasePage


class DashBoard(BasePage):
    main_button_xpath = "//ul/div[1]"
    players_button_xpath = "//ul/div[2]"
    translate_button_xpath = "//ul[2]/div[1]"
    sign_out_button_xpath = "//ul[2]/div[2]"
    team_contact_button_xpath = "//*[1][name()='a']"
    add_player_button_xpath = "//*[2][name()='a']"
    last_update_player_button_xpath = "//*[5][name()='a']"
    last_create_player_button_xpath = "//div[3]/div/div/a[1]/button/span[1]"
    icon_mainPage_xpath = "//*[@class = 'MuiSvgIcon-root jss23 jss24']"
    icon_players_xpath = "//*[@class = 'MuiSvgIcon-root jss23 jss25']"


