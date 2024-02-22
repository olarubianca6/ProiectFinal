from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage


class ButtonsPage(BasePage):

    URL_BUTTONS = "https://demoqa.com/buttons"
    BUTTON_DOUBLE_CLICK = (By.ID, "doubleClickBtn")
    SUCCESS_MSG_DOUBLE_CLICK = (By.ID, "doubleClickMessage")
    BUTTON_RIGHT_CLICK = (By.ID, "rightClickBtn")
    SUCCESS_MSG_RIGHT_CLICK = (By.ID, "rightClickMessage")


    def open(self):
        self.driver.get(self.URL_BUTTONS)

    def double_click_btn(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find(self.BUTTON_DOUBLE_CLICK))
        actions = ActionChains(self.driver)
        actions.double_click(self.find(self.BUTTON_DOUBLE_CLICK)).perform()

    def right_click_btn(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find(self.BUTTON_RIGHT_CLICK))
        self.driver.execute_script("arguments[0].oncontextmenu = function() { return false; }", self.find(self.BUTTON_RIGHT_CLICK))

        actions = ActionChains(self.driver)
        actions.context_click(self.find(self.BUTTON_RIGHT_CLICK)).perform()

    def is_double_click_msg_displayed(self):
        return self.find(self.SUCCESS_MSG_DOUBLE_CLICK).is_displayed()

    def is_right_click_msg_displayed(self):
        return self.find(self.SUCCESS_MSG_RIGHT_CLICK).is_displayed()

    def is_double_click_msg_correct(self, expected_text):
        assert expected_text == self.get_text(self.SUCCESS_MSG_DOUBLE_CLICK), "Double click message incorrect"

    def is_right_click_msg_correct(self, expected_text):
        assert expected_text == self.get_text(self.SUCCESS_MSG_RIGHT_CLICK), "Right click message incorrect"
