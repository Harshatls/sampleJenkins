from behave import *
from utils.basePage import driver,wait
from utils.testPage import testdata
import time
from loginSteps import basepage
# from selenium_utilities.selectors import XpathSelector
from selenium import webdriver
import subprocess

@when(u'Click on request access')
def step_impl(context):
    try:
        basepage.wait_and_find_and_click(testdata.requestAccessLocator,"xpath")
    except:
        raise NotImplementedError(u'STEP: When Click on request access')


@when(u'Click on PymetrikosUI app permissions')
def step_impl(context):
    try:
        basepage.wait_and_find_and_click(testdata.pymetrikosuiRequestAccessLocator,"xpath")
    except:
        raise NotImplementedError(u'STEP: When Click on PymetrikosUI app permissions')


@then(u'Click on request access for pymetrikosui permission and view permission for europe channel')
def step_impl(context):
    try:
        if basepage.is_element_present("xpath" , testdata.pymetrikosRequestButton):
            basepage.wait_and_find_and_click(testdata.pymetrikosRequestButton,"xpath")
        else:
            pass
        if basepage.is_element_present("xpath" , testdata.europeViewRequestButton):
            basepage.wait_and_find_and_click(testdata.europeViewRequestButton,"xpath")
        else:
            pass   
        subprocess.run(['behave','--tags','@grant_permission_to_apptest1'])
    except:
        raise NotImplementedError(u'STEP: Then Click on request access for pymetrikosui permission and view permission for europe channel')
    

@when(u'Click on esclation requests')
def step_impl(context):
    try:
        basepage.wait_and_find_and_click(testdata.escalationRequestsLocator,"xpath")
    except:
        raise NotImplementedError(u'STEP: When Click on esclation requests')

@then(u'Click on grant for all the permissions requested by apptest1')
def step_impl(context):
    try:
        for i in range(1,3):
            if basepage.is_element_present("xpath" , testdata.apptest1RequestsLocatorsList + "[1]"):
                time.sleep(2)
                basepage.wait_and_find_and_click(testdata.apptest1RequestsLocatorsList + "[1]","xpath")
                time.sleep(10)
        subprocess.run(['behave','--tags','@validate_apptest1_permission'])
    except:
        raise NotImplementedError(u'STEP: Then Click on grant for all the permissions requested by apptest1')
    
@when(u'Click on PymetrikosUI app')
def step_impl(context):
    try:
        basepage.wait_and_find_and_click(testdata.pymetrikosAppLocator,"xpath")
    except:
        raise NotImplementedError(u'STEP: When Click on PymetrikosUI app')


@then(u'Check whether user can view the rules of europe channel')
def step_impl(context):
    try:
        basepage.wait_and_find_and_click(testdata.pymetrikosChannelFilterLocator,"xpath")
        time.sleep(3)
        filterText = basepage.get_text_by_tag_or_xpath("option")
        if filterText == "EUROPE FB with Shopify":
            pass
        else:
            raise SystemExit("Europe channel rules cannot be viewed by user who has view access to Europe channel rules")
        subprocess.run(['behave','--tags','@reset_apptest1_permission'])
    except:
        raise NotImplementedError(u'STEP: Then Check whether user can view the rules of europe channel')

@when(u'Click on grant access')
def step_impl(context):
    try:
        basepage.wait_and_find_and_click(testdata.grantAccessLocator,"xpath")
    except:
        raise NotImplementedError(u'STEP: When Click on grant access')


@then(u'Remove PymetrikosUI and Europe view permissions for apptest1')
def step_impl(context):
    try:
        basepage.wait_and_find_and_click(testdata.apptest1grantaccessLocator,"xpath")
        time.sleep(2)
        basepage.wait_and_find_and_click(testdata.apptest1GrantAccessPymetrikosuiLocator,"xpath")
        time.sleep(2)
        basepage.wait_and_find_and_click(testdata.apptest1PymetrikosAppToggleLocator,"xpath")
        time.sleep(2)
        basepage.wait_and_find_and_click(testdata.apptest1PymetrikosEuropeToggleLocator,"xpath")
        time.sleep(2)
    except:
        raise NotImplementedError(u'STEP: Then Remove PymetrikosUI and Europe view permissions for apptest1')


@then(u'Click on request access for pymetrikosui permission and create permission')
def step_impl(context):
    try:
        if basepage.is_element_present("xpath" , testdata.pymetrikosRequestButton):
            basepage.wait_and_find_and_click(testdata.pymetrikosRequestButton,"xpath")
        else:
            pass
        if basepage.is_element_present("xpath" , testdata.europeCreateRequestButton):
            basepage.wait_and_find_and_click(testdata.europeCreateRequestButton,"xpath")
        else:
            pass   
        subprocess.run(['behave','--tags','@grant_permission_to_apptest2'])
    except:
        raise NotImplementedError(u'STEP: Then Click on request access for pymetrikosui permission and create permission')
    
@then(u'Click on grant for all the permissions requested by apptest2')
def step_impl(context):
    try:
        for i in range(1,3):
            if basepage.is_element_present("xpath" , testdata.apptest2RequestsLocatorsList + "[1]"):
                time.sleep(2)
                basepage.wait_and_find_and_click(testdata.apptest2RequestsLocatorsList + "[1]","xpath")
                time.sleep(10)
        subprocess.run(['behave','--tags','@validate_apptest2_permission'])
    except:
        raise NotImplementedError(u'STEP: Then Click on grant for all the permissions requested by apptest2')
    
@then(u'Check whether create a rule section and edit,delete,duplicate icons are available')
def step_impl(context):
    try:
        if basepage.is_element_present("xpath",testdata.createRuleLocator):
            pass
        else:
            raise SystemExit("Create a Rule form not available for user who has create rule permission")
        if basepage.is_element_present("xpath",testdata.editDeleteDuplicateLocators):
            pass
        else:
            raise SystemExit("Edit,Delete,Duplicate icons not visible to user who has create permission")
        subprocess.run(['behave','--tags','@reset_apptest2_permission'])
    except:
        raise NotImplementedError(u'STEP: Then Check whether create a rule section and edit,delete,duplicate icons are available')
    
@then(u'Remove PymetrikosUI and Europe view permissions for apptest2')
def step_impl(context):
    try:
        # driver.refresh()
        time.sleep(3)
        basepage.wait_and_find_and_click(testdata.apptest1grantaccessLocator,"xpath")
        time.sleep(2)
        basepage.wait_and_find_and_click(testdata.apptest1GrantAccessPymetrikosuiLocator,"xpath")
        time.sleep(2)
        basepage.wait_and_find_and_click(testdata.apptest1PymetrikosAppToggleLocator,"xpath")
        time.sleep(2)
        basepage.wait_and_find_and_click(testdata.apptest1PymetrikosEuropeCreateToggleLocator,"xpath")
        time.sleep(2)
    except:
        raise NotImplementedError(u'STEP: Then Remove PymetrikosUI and Europe view permissions for apptest2')