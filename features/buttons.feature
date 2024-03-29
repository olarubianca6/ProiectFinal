@ButtonsPage
Feature: Buttons

  Background: I open the Buttons page
    Given I am on the Buttons page

  @sanity
  Scenario: I verify the page URL and confirm cookies
    Then The URL is "<url>"
    #And I confirm cookies

  @sanity
  Scenario: I double click the double click button
    When I double click on the double click button
    Then Double click success message pops up
    And The message is "You have done a double click"

  @sanity
  Scenario: I right click on the right click button
    When I right click on the right click button
    Then Right click success message pops up
    And The message is "You have done a right click"
