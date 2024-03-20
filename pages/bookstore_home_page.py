from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BookstoreHomePage(BasePage):

    URL_HOME = "https://demoqa.com/books"
    GRID_CELLS_WITH_TEXT = (By.XPATH, "//*[@role='gridcell'][normalize-space(text())!='']")
    ERROR_SEARCH = (By.CLASS_NAME, "rt-noData")
    SEARCH_RESULT = (By.XPATH, '//*[@href="/books?book=9781449325862"]')

    def open(self):
        self.driver.get(self.URL_HOME)

    def url_verification(self):
        self.check_url(self.URL_HOME)

    def are_all_items_displayed(self):
        gridcells = self.driver.find_elements(*self.GRID_CELLS_WITH_TEXT)
        nr_of_items = len(gridcells)//2
        assert nr_of_items == 8, "Items not displayed correctly"

    def search_nonexisting_item(self):
        self.set_search_term("test")

    def is_search_error_displayed(self):
        self.is_element_displayed(self.ERROR_SEARCH)

    def search_existing_item(self):
        self.set_search_term("git")

    def is_search_result_correct(self):
        assert self.get_text(self.SEARCH_RESULT) == "Git Pocket Guide", "Search result incorrect"
