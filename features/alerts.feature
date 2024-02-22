@AlertsPage
Feature: Alerts Page

  Background: I open the Alerts page
    Given I am on the Alerts page
    And The URL is "https://demoqa.com/alerts"
    And I confirm cookies

  @sanity
  Scenario: I accept confirm box alert
    When I click the confirm box button
    And I click "ok" on the alert
    Then The result appears
    And The result is "You selected Ok"
