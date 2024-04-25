from behave import given, when, then
from selenium import webdriver
from utils.testPage import testdata
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utils.basePage import basePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.ui import  WebDriverWait
from utils.basePage import driver,wait


# object for the imported BasePage class and any method should be called using this object
basepage = basePage(driver,wait)


@given(u'I open a browser and open RBAC Login page')
def launch_browser(context):
    if testdata.BROWSER == 'chrome':
        # Maximize the chrome window 
        driver.maximize_window()
        # Opens the given URL page 
        driver.get(testdata.URL)
@when(u'I click on sign in RBAC link')
def step_impl(context):
    try:
        if basepage.is_element_present("xpath",testdata.rbacLoginButton):
            # Clicks on the login button on the RBAC login page 
            basepage.wait_and_find_and_click(testdata.rbacLoginButton,"xpath")
        else:
            pass
    except:
        raise NotImplementedError(u'STEP: When I click on sign in RBAC link')


@then(u'I enter the username and password to RBAC as tlsapp')
def step_impl(context):
    try:
        basepage.login_rbac(testdata.usernameFullAccess,testdata.passwordFullAccess)
    except:
        raise NotImplementedError(u'STEP: Then I enter the username and password to RBAC as tlsapp')
    
@when(u'I enter the username and password to RBAC as tlsapp')
def step_impl(context):
    try:
        basepage.login_rbac(testdata.usernameFullAccess,testdata.passwordFullAccess)
    except:
        raise NotImplementedError(u'STEP: When I enter the username and password to RBAC as tlsapp')
    
@given(u'I enter the username and password to RBAC as tlsapp')
def step_impl(context):
    try:
        basepage.login_rbac(testdata.usernameFullAccess,testdata.passwordFullAccess)
    except:
        raise NotImplementedError(u'STEP: Given I enter the username and password to RBAC as tlsapp')
    
@given(u'I enter the username and password to RBAC as apptest1')
def step_impl(context):
    try:
        basepage.login_rbac(testdata.usernameAppTest1,testdata.passwordAppTest1)
    except:
        raise NotImplementedError(u'STEP: Given I enter the username and password to RBAC as apptest1')
    
@when(u'I enter the username and password to RBAC as apptest1')
def step_impl(context):
    try:
        basepage.login_rbac(testdata.usernameAppTest1,testdata.passwordAppTest1)
    except:
        raise NotImplementedError(u'STEP: When I enter the username and password to RBAC as apptest1')
    
@then(u'I enter the username and password to RBAC as apptest1')
def step_impl(context):
    try:
        basepage.login_rbac(testdata.usernameAppTest1,testdata.passwordAppTest1)
    except:
        raise NotImplementedError(u'STEP: Then I enter the username and password to RBAC as apptest1')

@given(u'I enter the username and password to RBAC as apptest2')
def step_impl(context):
    try:
        basepage.login_rbac(testdata.usernameAppTest2,testdata.passwordAppTest2)
    except:
        raise NotImplementedError(u'STEP: Given I enter the username and password to RBAC as apptest2')
    
@when(u'I enter the username and password to RBAC as apptest2')
def step_impl(context):
    try:
        basepage.login_rbac(testdata.usernameAppTest2,testdata.passwordAppTest2)
    except:
        raise NotImplementedError(u'STEP: When I enter the username and password to RBAC as apptest2')
    
@then(u'I enter the username and password to RBAC as apptest2')
def step_impl(context):
    try:
        basepage.login_rbac(testdata.usernameAppTest2,testdata.passwordAppTest2)
    except:
        raise NotImplementedError(u'STEP: Then I enter the username and password to RBAC as apptest2')