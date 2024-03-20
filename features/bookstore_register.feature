@RegisterPage
Feature: Register Page

  Background: I open the Register page
    Given I am on the Register page

  @sanity
  Scenario: I verify the page URL and confirm cookies
    Then The URL is "<url>"
    #And I confirm cookies

  @negative @smoke
  Scenario: I try to register without completing required information
    When I click the register button
    Then All four required inputs are marked as invalid

   @smoke
   Scenario Outline: I register a new account
    When I type "<firstname>" in the firstname input
    And I type "<lastname>" in the lastname input
    And I type "<username>" in the username input
    And I type "<password>" in the password input
    And I click the captcha box
    Then Alert pops up

    Examples:
    | firstname | lastname | username |  password |
    | FirstName | LastName | tester   | Pa$$word12|
    | TestName  | TestName | pyta10   | Pa$$word9 |
