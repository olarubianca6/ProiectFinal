from behave import *


@given('I am on the WebTables page')
def step_impl(context):
    context.tables_page.open()


@when('I click the "First Name" button')
def step_impl(context):
    context.tables_page.click_first_name_btn()


@then('The rows should be alphabetically sorted by first name')
def step_impl(context):
    context.tables_page.are_rows_sorted_by_first_name()


@when('I click the "Age" button')
def step_impl(context):
    context.tables_page.click_age_btn()


@then('The rows should be sorted by age, from lowest to highest')
def step_impl(context):
    context.tables_page.are_rows_sorted_by_age()


