from behave import *


@given('I am on the Alerts page')
def step_impl(context):
    context.alerts_page.open()


@given('The URL is "https://demoqa.com/alerts"')
def step_impl(context):
    context.alerts_page.url_verification("https://demoqa.com/alerts")


@given('I confirm cookies')
def step_impl(context):
    context.alerts_page.confirm_cookies()


@when('I click the confirm box button')
def step_impl(context):
    context.alerts_page.click_alert_btn()


@when('I click "ok" on the alert')
def step_impl(context):
    context.alerts_page.accept_confirm_alert()


@then('The result appears')
def step_impl(context):
    assert context.alerts_page.is_alert_msg_displayed(), "Confirm alert result not displayed"


@then('The result is "You selected Ok"')
def step_impl(context):
    context.alerts_page.is_alert_msg_correct("You selected Ok")