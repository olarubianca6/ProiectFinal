from behave import *


@given('I am on the Buttons page')
def step_impl(context):
    context.buttons_page.open()


@given('The URL is "https://demoqa.com/buttons"')
def step_impl(context):
    context.buttons_page.url_verification("https://demoqa.com/buttons")


@when('I double click on the double click button')
def step_impl(context):
    context.buttons_page.double_click_btn()


@then('Double click success message pops up')
def step_impl(context):
    context.buttons_page.is_double_click_msg_displayed()


@then('The message is "You have done a double click"')
def step_impl(context):
    context.buttons_page.is_double_click_msg_correct("You have done a double click")


@when('I right click on the right click button')
def step_impl(context):
    context.buttons_page.right_click_btn()


@then('Right click success message pops up')
def step_impl(context):
    context.buttons_page.is_right_click_msg_displayed()


@then('The message is "You have done a right click"')
def step_impl(context):
    context.buttons_page.is_right_click_msg_correct("You have done a right click")
