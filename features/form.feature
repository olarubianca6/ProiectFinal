@FormPage
Feature: Practice Form

  Background: I open the Practice Form page
    Given I am on the Practice Form page

  @sanity
  Scenario: I verify the page URL and confirm cookies
    Then The URL is "<url>"
    #And I confirm cookies

  @smoke @regression
  Scenario: I successfully submit a form
    When I type a first name in the first name input
    And I type a last name in the last name input
    And I select a gender
    And I type a valid phone number in the mobile number input
    And I select a state
    And I select a city
    And I click the "Submit" button
    Then Pop-up with the form appears
    And The title is "Thanks for submitting the form"
