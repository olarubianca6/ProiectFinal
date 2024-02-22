@TablesPage
Feature: WebTables

  Background: I open the WebTables page
    Given I am on the WebTables page
    And The URL is "https://demoqa.com/webtables"
    And I confirm cookies

  @smoke
  Scenario: I sort the table by first name
    When I click the "First Name" button
    Then The rows should be alphabetically sorted by first name

  @smoke
  Scenario: I sort the table by age
    When I click the "Age" button
    Then The rows should be sorted by age, from lowest to highest