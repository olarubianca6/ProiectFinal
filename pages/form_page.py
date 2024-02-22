from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FormPage(BasePage):

    URL_FORM_PAGE = "https://demoqa.com/automation-practice-form"

    INPUT_FIRST_NAME = (By.XPATH, '//input[@id="firstName"]')
    INPUT_LAST_NAME = (By.XPATH, '//input[@id="lastName"]')
    SELECT_GENDER = (By.CSS_SELECTOR, 'label[for="gender-radio-1"].custom-control-label')
    INPUT_MOBILE_NR = (By.XPATH, '//input[@id="userNumber"]')
    SELECT_STATE = (By.ID, "state")
    SELECT_CITY = (By.ID, "city")
    BUTTON_SUBMIT = (By.XPATH, '//button[@id="submit"]')

    POP_UP_FORM = (By.CLASS_NAME, "modal-content")
    FORM_TITLE = (By.CLASS_NAME, "modal-title h4")


    def open(self):
        self.driver.get(self.URL_FORM_PAGE)

    def add_first_name(self, first_name):
        self.type(self.INPUT_FIRST_NAME, first_name)

    def add_last_name(self, last_name):
        self.type(self.INPUT_LAST_NAME, last_name)

    def select_gender(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find(self.SELECT_GENDER))
        self.click_btn(self.SELECT_GENDER)

    def add_mobile_nr(self, number):
        self.type(self.INPUT_MOBILE_NR, number)

    def select_state(self, state):
        self.select_by_text(self.SELECT_STATE, state)

    def select_city(self, city):
        self.select_by_text(self.SELECT_CITY, city)

    def submit_form(self):
        self.click_btn(self.BUTTON_SUBMIT)

    def is_form_displayed(self):
        return self.find(self.POP_UP_FORM).is_displayed()

    def is_form_title_correct(self, expected_text):
        assert expected_text == self.get_text(self.FORM_TITLE), "Form title incorrect"

