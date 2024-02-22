from behave import *


@given('I am on the bookstore home page')
def step_impl(context):
    context.bookstore_home_page.open()


@given('The URL is "https://demoqa.com/books"')
def step_impl(context):
    context.bookstore_register_page.url_verification("https://demoqa.com/books")


@then('8 books are displayed')
def step_impl(context):
    context.bookstore_home_page.are_all_items_displayed()


@when('I type "test" in the search input')
def step_impl(context):
    context.bookstore_home_page.set_search_term("test")


@then('No items found message appears')
def step_impl(context):
    assert context.bookstore_home_page.is_search_error_displayed(), "Search error not displayed"


@when('I type "git" in the search input')
def step_impl(context):
    context.bookstore_home_page.set_search_term("git")


@then('The result is "Git Pocket Guide"')
def step_impl(context):
    context.bookstore_home_page.is_search_result_correct("Git Pocket Guide")
