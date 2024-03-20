@HomePage
Feature: Book Store home page

  Background: I open the Book Store Home Page
    Given I am on the bookstore home page

  @sanity
  Scenario: I verify the page URL and confirm cookies
    Then The URL is "<url>"
    #And I confirm cookies

  Scenario: All items are displayed
    Then 8 books are displayed

  @negative @smoke
  Scenario: I search for a non-existing book
    When I type "test" in the search input
    Then No items found message appears

  @smoke
  Scenario: I search for an existing book
    When I type "git" in the search input
    Then The result is "Git Pocket Guide"
