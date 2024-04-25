@smoke
Feature:Smoke test cases
    Background:Login Steps
        Given I open a browser and open RBAC Login page
        When I click on sign in RBAC link
        Then I enter the username and password to RBAC as tlsapp
        And click on PymetrikosUI app
# TC # 3.4
@gotoconsole_smoke
Scenario:Go to console should redirect user back to Auth
    Given Click on go to console 
    Then Check whether user is redirected back to Auth or not

# TC # 3.5
@searchbox_smoke
Scenario:Check whether serch box is available or not
    Given Check for the search element in the Dashboard page

# TC # 3.6
@headers_list_smoke
Scenario:Check whether all the headers of the list are available or not
    Given Get all the headers of the list in the Dashboard page
    Then Check whether all the required headers are available or not

# TC # 4
@scroll_up_down_smoke
Scenario:User should be able to scroll up or down the screen
    Given Scroll up and down
        