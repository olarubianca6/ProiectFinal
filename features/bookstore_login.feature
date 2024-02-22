@LoginPage
Feature: Login Page

  Background: I open the Login page
    Given I am on the Login page
    And The URL is "https://demoqa.com/login"
    And I confirm cookies

  @negative @smoke
  Scenario Outline: I try to log in with unregistered account
    When I type "<username>" in the username input
    And I type "<password>" in the password input
    And I click the login button
    Then Login error message appears

    Examples:
    | username | password |
    | pyta10   | pass123  |
    | testing  | testpass9|
