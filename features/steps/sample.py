from behave import given, when, then
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.ui import  WebDriverWait

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver,30)

# # object for the imported BasePage class and any method should be called using this object
# basepage = basePage(driver,wait)


@given(u'I open the browser')
def launch_browser(context):
    
        # Maximize the chrome window 
        driver.maximize_window()
        # Opens the given URL page 
        driver.get("www.google.com")


