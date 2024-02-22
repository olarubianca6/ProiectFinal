@RegisterPage
Feature: Register Page

  Background: I open the Register page
    Given I am on the Register page
    And The URL is "https://demoqa.com/register"
    And I confirm cookies

  @negative @smoke
  Scenario: I try to register without completing required information
    When I click the register button
    Then All four required inputs are marked as invalid