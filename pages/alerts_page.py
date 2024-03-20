from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException, NoAlertPresentException
from pages.base_page import BasePage


class AlertsPage(BasePage):

    URL_ALERTS = "https://demoqa.com/alerts"
    BUTTON_ALERT_CONFIRM = (By.ID, "confirmButton")
    ALERT_SUCCESS_MSG = (By.CLASS_NAME, "text-success")

    def open(self):
        self.driver.get(self.URL_ALERTS)

    def url_verification(self):
        self.check_url(self.URL_ALERTS)

    def click_alert_btn(self):
        self.click_btn(self.BUTTON_ALERT_CONFIRM)

    def accept_confirm_alert(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            print("No alert found")
        except NoAlertPresentException:
            print("No alert found")

    def is_alert_msg_displayed(self):
        self.is_element_displayed(self.ALERT_SUCCESS_MSG)

    def is_alert_msg_correct(self):
        assert self.get_text(self.ALERT_SUCCESS_MSG) == "You selected Ok", "Alert message incorrect"
