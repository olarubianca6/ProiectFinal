from selenium.webdriver.common.by import By

from browser import Browser


class BasePage(Browser):

    INPUT_SEARCH = (By.ID, "searchBox")
    BUTTON_CONFIRM_COOKIES = (By.CLASS_NAME, "fc-button-label")
    cookies_confirmed = False

    def find(self, locator):
        return self.driver.find_element(*locator)

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def get_text_from_element(self, element):
        return element.text

    def click_btn(self, locator):
        self.find(locator).click()

    def confirm_cookies(self):
        if not self.cookies_confirmed:
            self.click_btn(self.BUTTON_CONFIRM_COOKIES)
            self.cookies_confirmed = True

    def url_verification(self, expected_url):
        return self.driver.current_url == expected_url

    def set_search_term(self, text):
        self.type(self.INPUT_SEARCH, text)
