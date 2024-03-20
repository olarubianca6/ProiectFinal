from behave import *


@given('I am on the Practice Form page')
def step_impl(context):
    context.form_page.open()


@when('I type a first name in the first name input')
def step_impl(context):
    context.form_page.add_first_name()


@when('I type a last name in the last name input')
def step_impl(context):
    context.form_page.add_last_name()


@when('I select a gender')
def step_impl(context):
    context.form_page.select_gender()


@when('I type a valid phone number in the mobile number input')
def step_impl(context):
    context.form_page.add_mobile_nr()


@when('I select a state')
def step_impl(context):
    context.form_page.select_state()


@when('I select a city')
def step_impl(context):
    context.form_page.select_city()


@when('I click the "Submit" button')
def step_impl(context):
    context.form_page.submit_form()


@then('Pop-up with the form appears')
def step_impl(context):
    context.form_page.is_form_displayed()


@then('The title is "Thanks for submitting the form"')
def step_impl(context):
    context.form_page.is_form_title_correct()
