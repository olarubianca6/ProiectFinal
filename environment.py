from browser import Browser

from pages.alerts_page import AlertsPage
from pages.buttons_page import ButtonsPage
from pages.form_page import FormPage
from pages.tables_page import TablesPage
from pages.bookstore_login_page import BookstoreLoginPage
from pages.bookstore_register_page import BookstoreRegisterPage
from pages.bookstore_home_page import BookstoreHomePage


def before_all(context):
    context.browser = Browser()
    context.alerts_page = AlertsPage()
    context.buttons_page = ButtonsPage()
    context.form_page = FormPage()
    context.tables_page = TablesPage()
    context.bookstore_login_page = BookstoreLoginPage()
    context.bookstore_register_page = BookstoreRegisterPage()
    context.bookstore_home_page = BookstoreHomePage()


def after_all(context):
    context.browser.close()


def before_scenario(context, scenario):
    context.cookies_confirmed = False


def after_scenario(context, scenario):
    pass


def on_exception(context, feature, scenario, step, step_func, exception):
    print(f'Step failed: {step.name}. Exception: {exception}')
