from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class FormPage(BasePage):

    URL_FORM_PAGE = "https://demoqa.com/automation-practice-form"

    INPUT_FIRST_NAME = (By.XPATH, '//input[@id="firstName"]')
    INPUT_LAST_NAME = (By.XPATH, '//input[@id="lastName"]')
    SELECT_GENDER = (By.CSS_SELECTOR, 'label[for="gender-radio-1"].custom-control-label')
    INPUT_MOBILE_NR = (By.XPATH, '//input[@id="userNumber"]')
    SELECT_STATE = (By.ID, "state")
    SELECT_CITY = (By.ID, "city")
    DROPDOWN = (By.CLASS_NAME, "css-26l3qy-menu")
    BUTTON_SUBMIT = (By.XPATH, '//button[@id="submit"]')

    POP_UP_FORM = (By.CLASS_NAME, "modal-content")
    FORM_TITLE = (By.CLASS_NAME, "modal-title")

    def open(self):
        self.driver.get(self.URL_FORM_PAGE)

    def url_verification(self):
        self.check_url(self.URL_FORM_PAGE)

    def add_first_name(self):
        self.type(self.INPUT_FIRST_NAME, "TestFirstName")

    def add_last_name(self):
        self.type(self.INPUT_LAST_NAME, "TestLastName")

    def select_gender(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find(self.SELECT_GENDER))
        self.click_btn(self.SELECT_GENDER)

    def add_mobile_nr(self):
        self.type(self.INPUT_MOBILE_NR, "1234567890")

    def select_state(self):
        self.click_btn(self.SELECT_STATE)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.DROPDOWN))
        self.click_btn(self.DROPDOWN)

    def select_city(self):
        self.click_btn(self.SELECT_CITY)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.DROPDOWN))
        self.click_btn(self.DROPDOWN)

    def submit_form(self):
        self.click_btn(self.BUTTON_SUBMIT)

    def is_form_displayed(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.POP_UP_FORM))
        self.is_element_displayed(self.POP_UP_FORM)

    def is_form_title_correct(self):
        assert self.get_text(self.FORM_TITLE) == "Thanks for submitting the form", "Form title incorrect"
