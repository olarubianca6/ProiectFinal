@TablesPage
Feature: WebTables

  Background: I open the WebTables page
    Given I am on the WebTables page

  @sanity
  Scenario: I verify the page URL and confirm cookies
    Then The URL is "<url>"
    #And I confirm cookies

  @smoke
  Scenario: I sort the table by first name
    When I click the "First Name" button
    Then The rows should be alphabetically sorted by first name

  @smoke
  Scenario: I sort the table by age
    When I click the "Age" button
    Then The rows should be sorted by age, from lowest to highest
