from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class BookstoreRegisterPage(BasePage):

    URL_REGISTER = "https://demoqa.com/register"
    BUTTON_REGISTER = (By.ID, "register")
    ERRORS_REGISTER = (By.CLASS_NAME, "is-invalid")

    INPUT_FIRSTNAME = (By.ID, "firstname")
    INPUT_LASTNAME = (By.ID, "lastname")
    CAPTCHA_BOX = (By.CLASS_NAME, "rc-anchor-content")

    def open(self):
        self.driver.get(self.URL_REGISTER)

    def url_verification(self):
        self.check_url(self.URL_REGISTER)

    def click_register_btn(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find(self.BUTTON_REGISTER))
        self.click_btn(self.BUTTON_REGISTER)

    def are_errors_displayed(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find(self.ERRORS_REGISTER))
        invalid_inputs = self.driver.find_elements(*self.ERRORS_REGISTER)
        assert len(invalid_inputs) == 4, "Registration errors not displayed"

    def add_firstname(self, firstname):
        self.type(self.INPUT_FIRSTNAME, firstname)

    def add_lastname(self, lastname):
        self.type(self.INPUT_LASTNAME, lastname)

    def click_captcha(self):
        WebDriverWait(self.driver, 5)
        self.driver.execute_script("arguments[0].click();", self.find(self.CAPTCHA_BOX))

    def alert_verification(self):
        assert WebDriverWait(self.driver, 5).until(EC.alert_is_present()), "Alert not present"
        