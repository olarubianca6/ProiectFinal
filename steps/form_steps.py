from behave import *


@given('I am on the Practice Form page')
def step_impl(context):
    context.form_page.open()


@given('The URL is "https://demoqa.com/automation-practice-form"')
def step_impl(context):
    context.form_page.url_verification("https://demoqa.com/automation-practice-form")


@when('I type "FirstName" in the first name input')
def step_impl(context):
    context.form_page.add_first_name("FirstName")


@when('I type "LastName" in the last name input')
def step_impl(context):
    context.form_page.add_last_name("LastName")


@when('I select a gender')
def step_impl(context):
    context.form_page.select_gender()


@when('I type "1234567890" in the mobile number input')
def step_impl(context):
    context.form_page.add_mobile_nr("1234567890")


@when('I select a state')
def step_impl(context):
    context.form_page.select_state("NCR")


@when('I select a city')
def step_impl(context):
    context.form_page.select_city("Delhi")


@when('I click the "Submit" button')
def step_impl(context):
    context.form_page.submit_form()


@then('Pop-up with the form appears')
def step_impl(context):
    assert context.form_page.is_form_displayed(), "Pop-up form not displayed"


@then('The title is "Thanks for submitting the form"')
def step_impl(context):
    context.form_page.is_form_title_correct("Thanks for submitting the form")
