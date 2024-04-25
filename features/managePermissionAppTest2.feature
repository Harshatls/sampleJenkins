Feature:UI test cases
    Background:Login Steps
        Given I open a browser and open RBAC Login page
        When I click on sign in RBAC link

@request_apptest2_permission
Scenario:Log in as apptest2 check permission for apptest1
    Given I enter the username and password to RBAC as apptest2
    When Click on request access
    And Click on PymetrikosUI app permissions
    Then Click on request access for pymetrikosui permission and create permission

@grant_permission_to_apptest2
Scenario:Log in as tlsapp manager and grant access for the same
    Given I enter the username and password to RBAC as tlsapp
    When Click on esclation requests
    Then Click on grant for all the permissions requested by apptest2
@validate_apptest2_permission
Scenario:Log in as apptest1 to view pymetrikosui
    Given I enter the username and password to RBAC as apptest2
    When Click on PymetrikosUI app 
    Then Check whether create a rule section and edit,delete,duplicate icons are available

@reset_apptest2_permission
Scenario:Log in as tlsapp and reset permissions for apptest2
    Given I enter the username and password to RBAC as tlsapp
    When Click on grant access
    Then Remove PymetrikosUI and Europe view permissions for apptest2