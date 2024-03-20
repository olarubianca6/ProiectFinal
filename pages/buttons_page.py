from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class ButtonsPage(BasePage):

    URL_BUTTONS = "https://demoqa.com/buttons"
    BUTTON_DOUBLE_CLICK = (By.ID, "doubleClickBtn")
    SUCCESS_MSG_DOUBLE_CLICK = (By.ID, "doubleClickMessage")
    BUTTON_RIGHT_CLICK = (By.ID, "rightClickBtn")
    SUCCESS_MSG_RIGHT_CLICK = (By.ID, "rightClickMessage")

    def open(self):
        self.driver.get(self.URL_BUTTONS)

    def url_verification(self):
        self.check_url(self.URL_BUTTONS)

    def double_click_btn(self):
        WebDriverWait(self.driver, 5)
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find(self.BUTTON_DOUBLE_CLICK))
        actions = ActionChains(self.driver)
        actions.double_click(self.find(self.BUTTON_DOUBLE_CLICK)).perform()

    def right_click_btn(self):
        WebDriverWait(self.driver, 5)
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find(self.BUTTON_RIGHT_CLICK))
        self.driver.execute_script("arguments[0].oncontextmenu = function() { return false; }",
                                   self.find(self.BUTTON_RIGHT_CLICK))
        actions = ActionChains(self.driver)
        actions.context_click(self.find(self.BUTTON_RIGHT_CLICK)).perform()

    def is_double_click_msg_displayed(self):
        self.is_element_displayed(self.SUCCESS_MSG_DOUBLE_CLICK)

    def is_right_click_msg_displayed(self):
        self.is_element_displayed(self.SUCCESS_MSG_RIGHT_CLICK)

    def is_double_click_msg_correct(self):
        assert self.get_text(self.SUCCESS_MSG_DOUBLE_CLICK) == "You have done a double click", \
            "Double click message incorrect"

    def is_right_click_msg_correct(self):
        assert self.get_text(self.SUCCESS_MSG_RIGHT_CLICK) == "You have done a right click", \
            "Right click message incorrect"
