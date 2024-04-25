@function
Feature:Funtional test cases
    Background:Login Steps
        Given I open a browser and open RBAC Login page
        When I click on sign in RBAC link
        Then I enter the username and password to RBAC as tlsapp
        And click on PymetrikosUI app
    
@status_toggle
Scenario:Verify that users can successfully sort the rules list based on the Active or  Active&Inactive status
    Given Count the number of rules that are both active and Inactive before sorting
    When Click on the status toggle
    Then Count the number of rules that are in the list

@open_create_form
Scenario:Verify that clicking on the Create a Rule option opens the rule addition form
    Given Click on Create a rule
    When Check whether the form is opened or not

@create_rule_contents
Scenario:Verify whether create rule form contains all the fields
    Given Click on Create a rule
    When Check whether all the fields are present or not

@enter_rule_name
Scenario:Verify that users can successfully enter a rule name in the Rule Add form
    Given Click on Create a rule
    When Click on the input field to enter a new rule name
    Then Type a rule name and check whether entered rule name is visible or not

@task_to_perform
Scenario:Verify whether user is able to select an option from the task to perform dropdown
    Given Click on Create a rule
    When User clicks on task to perform dropdown and click on pause
    Then Check whether when selected pause only pause is visible

@include_keywords_section
Scenario:Verify that users can successfully enter Campaign, Adset, and Ad keywords in the 'Include Keyword' section
    Given Click on Create a rule
    When Enter an Campaign in Include keywords section
    And Enter an Adset in Include keywords section
    And Enter an Ad in Include keywords section
    Then Check whether the entered Include keywords are in the input fields or not

@exclude_keywords_section
Scenario:Verify that users can successfully enter Campaign, Adset, and Ad keywords in the 'Exclude Keyword' section
    Given Click on Create a rule
    When Enter an Campaign in Exclude keywords section
    And Enter an Adset in Exclude keywords section
    And Enter an Ad in Exclude keywords section
    Then Check whether the entered Exclude keywords are in the input fields or not

@add_filter_string
Scenario:Verify that users can add multiple filter strings by clicking on the 'Add Filter String' button
    Given Click on Create a rule
    When Click on Add filter string button
    Then Check whether the new filter string is added or not

@remove_filter_string
Scenario:Verify that users can remove a filter string section by clicking on the close icon only when more than one filter section is present
    Given Click on Create a rule
    When Check for the remove filter string button
    And If not present click on the Add filter string 
    Then Check for the remove filter string button

@select_fb_accounts_dropdown
Scenario:Verify that users can select a Facebook account. Upon clicking, the drop-down should open, and after selection, the chosen element should be visible in the field
    Given Click on Create a rule
    When Click on select fb account dropdown
    And Select any account from the dropdown
    Then Check selected account is shown in the field or not

@logged_in_user
Scenario:Verify that the 'Logged In' field displays the username of the user who has logged in
    Given Click on Create a rule
    When Check whether the logged in user element is available or not
    Then Check whether the name shown in the field matches with the logged in user

@error_for_mandatory_fields
Scenario:Verify that error is shown below those mandatory fields those are not filled
    Given Click on Create a rule
    When Click on 'Create button'
    Then Check for the error on the page

@for_last_field
Scenario:Verify that the 'For Last' field in the condition section accepts numbers and does not allow values except numbers between 0 and 31 and -1
    Given Click on Create a rule
    When Input a letter in the for last field 
    And Check for the error when entered letter
    And Input a number greater than 30 
    And Check for the error when entered number greater than 30
    And Input a number less than -1 
    Then check for the error when entered number less than -1

@greater_than_field
Scenario:Verify that users can successfully enter numbers in the 'Greater Than' field in the condition section
    Given Click on Create a rule
    When Input a number in the greater than field
    Then Check whether the error is shown or not

@less_than_field_roas
Scenario:Verify that Error is shown when user enters negative numbers in the Less than ROAS field
    Given Click on Create a rule
    When Input a number in the less than ROAS field
    Then Check whether the ROAS error is shown or not

@cancel_button
Scenario:Verify that clicking on the Cancel button from the Add Rule page redirects the user back to the dashboard view page
    Given Click on Create a rule
    When Click on the cancel button 
    Then Check whether the user is redirected back to PymetrikosUI home page or not

@switch_channel_while_create_rule
Scenario:Verify whether when user switches to other channel filters ,User should be redirected to respective channels dashboard page
    Given Click on Create a rule
    When Click on channel filter and click on another channel
    Then check whether the user is redirected back to dashboard page or not

@freeze_search_bar
Scenario:Verify search bar is freezed on the screen when scrolled up or down
    Given Scroll down the page
    Then Check whether user is still able to see the search bar or not
