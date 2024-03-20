from behave import *


@given('I am on the Register page')
def step_impl(context):
    context.bookstore_register_page.open()


@when('I click the register button')
def step_impl(context):
    context.bookstore_register_page.click_register_btn()


@then('All four required inputs are marked as invalid')
def step_impl(context):
    context.bookstore_register_page.are_errors_displayed()


@when('I type "{firstname}" in the firstname input')
def step_impl(context, firstname):
    context.bookstore_register_page.add_firstname(firstname)


@when('I type "{lastname}" in the lastname input')
def step_impl(context, lastname):
    context.bookstore_register_page.add_lastname(lastname)


@when('I click the captcha box')
def step_impl(context):
    context.bookstore_register_page.click_captcha()


@then('Alert pops up')
def step_impl(context):
    context.bookstore_register_page.alert_verification()
