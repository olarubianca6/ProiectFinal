from behave import *


@given('I am on the Login page')
def step_impl(context):
    context.bookstore_login_page.open()


@when('I type "{username}" in the username input')
def step_impl(context, username):
    context.bookstore_login_page.add_username(username)


@when('I type "{password}" in the password input')
def step_impl(context, password):
    context.bookstore_login_page.add_password(password)


@when('I click the login button')
def step_impl(context):
    context.bookstore_login_page.click_login_btn()


@then('Login error message appears')
def step_impl(context):
    context.bookstore_login_page.is_error_msg_displayed()
