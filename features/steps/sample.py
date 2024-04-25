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

# basepage.wait_and_find_and_click("")

@given(u'Sample')
def launch_browser(context):
    driver.get("www.google.com")