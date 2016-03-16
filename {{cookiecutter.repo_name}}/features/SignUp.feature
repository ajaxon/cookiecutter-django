# Created by Allen at 2/2/16
@profile
Feature: Signup
  # Enter feature description here

  Background:
    Given I am on the "account_signup" page
  Scenario: I successfully register

    Then I should see "Register"
    When I click "register"
    Then I should see "text"
    And  I should be sent an email
    #And  I should be on the "home" page

  @whip
  Scenario Outline: I try to register with bad input
    When I fill in "username" with "<username>"
    And  I fill in "email" with "<email>"
    And  I fill in "password1" with "<password1>"
    And  I fill in "password2" with "<password2>"
    And  I click "register"
    Then I should see "<error>"

    Examples: Bad username
      | username | email | password1 | password2 | error |
      |  N/A     | test@email.com  | testpass     |     testpass  |  This field is required    |
      | admin    | test@email.com  | testpass    |     testpass  |  Username can not be used     |
      | joe    | test@email.com  | testpass    |     testpass  |  at least 5    |

    Examples: Bad email
      | username | email | password1 | password2 | error |
      |  testusername     | test@email  | testpass     |     testpass  |  enter a valid email    |
      | testusername    | @email.com  | testpass    |     testpass  |  enter a valid email     |
      | testusername    | testemail.com  | testpass    |     testpass  |  enter a valid email    |
      | testusername    | test@email.chicken  | testpass    |     testpass  |  enter a valid email    |


    Examples: Bad password
      | username | email | password1 | password2 | error |
      |  testusername     | test@email.com  | testpass     |     testposs  |  type same password    |
      |  testusername     | test@email.com  | pass     |     pass  |  minimum of 6    |
      | testusername      | test@email.com  | password | password  | common           |


  Scenario: User tries to register with taken username
    Given A user exists with username "testuser" email "test@email.com"
    When I fill in "username" with "testuser"
    And  I fill in "email" with "test@email.com"
    And  I fill in "password1" with "testpass"
    And  I fill in "password2" with "testpass"
    And  I click "register"
    Then I should see "username is already taken"
    And  I should see "already registered with this e-mail"
