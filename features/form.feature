@FormPage
Feature: Practice Form

  Background: I open the Practice Form page
    Given I am on the Practice Form page
    And The URL is "https://demoqa.com/automation-practice-form"
    And I confirm cookies

  @smoke @regression
  Scenario: I successfully submit a form
    When I type "FirstName" in the first name input
    And I type "LastName" in the last name input
    And I select a gender
    And I type "1234567890" in the mobile number input
    And I select a state
    And I select a city
    And I click the "Submit" button
    Then Pop-up with the form appears
    And The title is "Thanks for submitting the form"
