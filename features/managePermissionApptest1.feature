Feature:Role/Permission based test cases
    Background:Login Steps
        Given I open a browser and open RBAC Login page
        When I click on sign in RBAC link
# TC # 6.1
# The below scenarios are dependent scenarios starting from the first one 
# Run the first scenario to run the all scenarios
# login as apptest1 check whether the permission for pymetrikos is there or not , if not give permission amd check
@request_apptest1_permission
Scenario:Log in as apptest1 check permission for apptest1
    Given I enter the username and password to RBAC as apptest1
    When Click on request access 
    And Click on PymetrikosUI app permissions
    Then Click on request access for pymetrikosui permission and view permission for europe channel
@grant_permission_to_apptest1
Scenario:Log in as tlsapp manager and grant access for the same
    Given I enter the username and password to RBAC as tlsapp
    When Click on esclation requests
    Then Click on grant for all the permissions requested by apptest1
@validate_apptest1_permission
Scenario:Log in as apptest1 to view pymetrikosui
    Given I enter the username and password to RBAC as apptest1
    When Click on PymetrikosUI app 
    Then Check whether user can view the rules of europe channel
@reset_apptest1_permission
Scenario:Log in as tlsapp and reset permissions for apptest1
    Given I enter the username and password to RBAC as tlsapp
    When Click on grant access
    Then Remove PymetrikosUI and Europe view permissions for apptest18

# @request_javvaji_permission
# Scenario:Log in as apptest1 check permission for apptest1
#     Given I enter the username and password to RBAC as apptest1
#     When Click on request access 
#     And Click on Docustack app permissions
#     Then Click on request access for pymetrikosui permission and view permission for europe channel
@grant_permission_to_javvaji
Scenario:Log in as tlsapp manager and grant access for the same
    Given I enter the username and password to RBAC as tlsapp
    When Click on grant access
    Then Grant all the permissions