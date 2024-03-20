from behave import *


@given('I am on the bookstore home page')
def step_impl(context):
    context.bookstore_home_page.open()


@then('8 books are displayed')
def step_impl(context):
    context.bookstore_home_page.are_all_items_displayed()


@when('I type "test" in the search input')
def step_impl(context):
    context.bookstore_home_page.search_nonexisting_item()


@then('No items found message appears')
def step_impl(context):
    context.bookstore_home_page.is_search_error_displayed()


@when('I type "git" in the search input')
def step_impl(context):
    context.bookstore_home_page.search_existing_item()


@then('The result is "Git Pocket Guide"')
def step_impl(context):
    context.bookstore_home_page.is_search_result_correct()
