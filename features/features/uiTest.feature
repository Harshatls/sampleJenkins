@ui
Feature:UI test cases
    Background:Login Steps
        Given I open a browser and open RBAC Login page
        When I click on sign in RBAC link
        Then I enter the username and password to RBAC as tlsapp
        And click on PymetrikosUI app
    
# TC # 1
# Not needed as already covered in test case 3.6
# @dashboard_ui
# Scenario: Dashboard page is opened or not when clicked on PymetrikosUI in RBAC
#  Given Collect the text of the columns present
#   When Check whether the columns are same as the columns in Dashboard

# TC # 2
# @alignment_ui

# TC # 3.1
@logo_ui
Scenario:Check whether the logo is present or not
    Given Check whether logo is present or not

# TC # 3.2
@navigation_left_ui
Scenario:Check whether the navigation bar contains Dashboard and Create a rule sections
    Given Get contents of the side bar 
    When Check whether they are same as Dashboard and Create a rule

# TC # 3.3
@shopify_channel_filter_ui
Scenario:Check whether the shopify channel filter is available or not
    Given Check whether the channel filter is available or not
