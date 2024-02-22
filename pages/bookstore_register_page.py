from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BookstoreRegisterPage(BasePage):

    URL_REGISTER = "https://demoqa.com/register"
    BUTTON_REGISTER = (By.ID, "register")
    ERRORS_REGISTER = (By.CLASS_NAME, "is-invalid")

    def open(self):
        self.driver.get(self.URL_REGISTER)

    def click_register_btn(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find(self.BUTTON_REGISTER))
        self.click_btn(self.BUTTON_REGISTER)

    def are_errors_displayed(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find(self.ERRORS_REGISTER))
        invalid_inputs = self.driver.find_elements(*self.ERRORS_REGISTER)
        assert len(invalid_inputs) == 4, "Registration errors not displayed"
        