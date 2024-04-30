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
from loginSteps import basepage

@given(u'Get contents of the side bar')
def step_impl(context):
    try:
        global dashboardText,createARuleText
        dashboardText = basepage.get_text_by_xpath(testdata.dashboardSideBarLocator,"xpath")
        createARuleText = basepage.get_text_by_xpath(testdata.createARuleLocator,"xpath")

    except:
        raise NotImplementedError(u'STEP: Given Get contents of the side bar')


@when(u'Check whether they are same as Dashboard and Create a rule')
def step_impl(context):
    try:
        basepage.wait_and_find(testdata.createARuleLocator,"xpath")
        if dashboardText == "Dashboard" and createARuleText == "Create a Rule":
            pass
        else:
            raise SystemExit("Side bar does not contain sections as per the requirement")
    except:
        raise NotImplementedError(u'STEP: When Check whether they are same as Dashboard and Create a rule')
    
@given(u'Check whether the channel filter is available or not')
def step_impl(context):
    try:
        basepage.wait_and_find(testdata.shopifyChannelFilterLocator,"xpath")
    except:
        raise NotImplementedError(u'STEP: Given Check whether the channel filter is available or not')

@given(u'Check whether logo is present or not')
def step_impl(context):
    try:
        basepage.wait_and_find(testdata.logoLocator,"xpath")
        if basepage.is_element_present("xpath",testdata.logoLocator):
            pass
        else:
            raise SystemExit("Logo not present after clicking on PymetrikosUI app")
    except:
        raise NotImplementedError(u'STEP: Given Check whether logo is present or not')