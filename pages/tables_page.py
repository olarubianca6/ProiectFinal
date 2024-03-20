from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TablesPage(BasePage):

    URL_TABLES = "https://demoqa.com/webtables"
    BUTTON_FIRST_NAME = (By.XPATH, '//*[text()="First Name"]')
    BUTTON_AGE = (By.XPATH, '//*[contains(text(), "Age")]')

    def open(self):
        self.driver.get(self.URL_TABLES)

    def url_verification(self):
        self.check_url(self.URL_TABLES)

    def click_first_name_btn(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find(self.BUTTON_FIRST_NAME))
        self.click_btn(self.BUTTON_FIRST_NAME)

    def are_rows_sorted_by_first_name(self):
        table_cells = self.driver.find_elements(By.CLASS_NAME, "rt-td")
        first_name_cells = [self.get_text_from_element(table_cells[0]), self.get_text_from_element(table_cells[7]),
                            self.get_text_from_element(table_cells[14])]
        sorted_rows = sorted(first_name_cells)
        assert first_name_cells == sorted_rows, "First name cells not sorted correctly"

    def click_age_btn(self):
        self.click_btn(self.BUTTON_AGE)

    def are_rows_sorted_by_age(self):
        table_cells = self.driver.find_elements(By.CLASS_NAME, "rt-td")
        age_cells = [self.get_text_from_element(table_cells[2]), self.get_text_from_element(table_cells[9]),
                     self.get_text_from_element(table_cells[16])]
        sorted_rows = sorted(age_cells)
        assert age_cells == sorted_rows, "Age cells not sorted correctly"
