from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BookstoreLoginPage(BasePage):

    URL_LOGIN = "https://demoqa.com/login"
    INPUT_USERNAME = (By.ID, "userName")
    INPUT_PASSWORD = (By.ID, "password")
    BUTTON_LOGIN = (By.ID, "login")
    LOGIN_ERROR_MSG = (By.ID, "name")

    def open(self):
        self.driver.get(self.URL_LOGIN)

    def url_verification(self):
        self.check_url(self.URL_LOGIN)

    def add_username(self, username):
        self.type(self.INPUT_USERNAME, username)

    def add_password(self, password):
        self.type(self.INPUT_PASSWORD, password)

    def click_login_btn(self):
        self.click_btn(self.BUTTON_LOGIN)

    def is_error_msg_displayed(self):
        self.is_element_displayed(self.LOGIN_ERROR_MSG)
