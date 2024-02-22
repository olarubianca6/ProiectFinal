from behave import *


@given('I am on the Register page')
def step_impl(context):
    context.bookstore_register_page.open()


@given('The URL is "https://demoqa.com/register"')
def step_impl(context):
    context.bookstore_register_page.url_verification("https://demoqa.com/register")


@when('I click the register button')
def step_impl(context):
    context.bookstore_register_page.click_register_btn()


@then('All four required inputs are marked as invalid')
def step_impl(context):
    context.bookstore_register_page.are_errors_displayed()

