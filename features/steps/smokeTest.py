import time
from behave import given, when, then
import pyautogui
from selenium import webdriver
from utils.testPage import testdata
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utils.basePage import basePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.ui import  WebDriverWait
from loginSteps import basepage,driver,wait

@given(u'Click on go to console')
def step_impl(context):
    try:
        basepage.wait_and_find_and_click(testdata.goToConsoleLocator,"xpath")
    except:
        raise NotImplementedError(u'STEP: Given Click on go to console')


@then(u'Check whether user is redirected back to Auth or not')
def step_impl(context):
    try:
        basepage.wait_and_find(testdata.yourAppsLocator,"xpath")
        if basepage.is_element_present("xpath",testdata.yourAppsLocator):
            pass
        else:
            raise SystemExit("User is not directed back to Auth when clicked on Go to console")
    except:
        raise NotImplementedError(u'STEP: Then Check whether user is redirected back to Auth or not')
    
@given(u'Check for the search element in the Dashboard page')
def step_impl(context):
    try:
        basepage.wait_and_find_and_click(testdata.searchBoxLocator,"xpath")
        if basepage.is_element_present("xpath",testdata.searchBoxLocator):
            pass
        else:
            raise SystemExit("Search box is not present in the dashboard screen")
    except:
        raise NotImplementedError(u'STEP: Given Check for the search element in the Dashboard page')

@given(u'Get all the headers of the list in the Dashboard page')
def step_impl(context):
    try:
        global headersTextList
        basepage.wait_and_find(testdata.headerLocatorsList,"xpath")
        headersTextList = basepage.get_text_in_a_list_for_given_list_locator(testdata.headerLocatorsList)
    except:
        raise NotImplementedError(u'STEP: Given Get all the headers of the list in the Dashboard page')


@then(u'Check whether all the required headers are available or not')
def step_impl(context):
    try:
        if len(testdata.headersToBePresent) == len(headersTextList):
            pass
        for i in testdata.headersToBePresent:
            if i in headersTextList:
                pass
            else:
                raise SystemExit("All the headers are not present in the dashboard page")
    except:
        raise NotImplementedError(u'STEP: Then Check whether all the required headers are available or not')
    
@given(u'Scroll up and down')
def step_impl(context):
    try:
        basepage.wait_and_find(testdata.editDeleteDuplicateLocators,"xpath")
        basepage.scroll_down
        time.sleep(4)
    except:
        raise NotImplementedError(u'STEP: Given Scroll up and down')
    

@then(u'Grant all the permissions')
def step_impl(context):
    try:
        basepage.wait_and_find_and_click(testdata.harshaProfileLocator,"xpath")
        basepage.wait_and_find_and_click(testdata.docustackLocator,"xpath")
        for i in range(1,297):
            ele = testdata.toggleListLocator + f"[{i}]"
            basepage.wait_and_find_and_click(ele,"xpath")
            time.sleep(3)
    except:
        raise NotImplementedError(u'STEP: Then Grant all the permissions')