import os
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui as pag
from bs4 import BeautifulSoup
from utils.testPage import testdata
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class basePage():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
    @staticmethod
    def write_to_file(result):
        with open("results.txt", "a") as file:
            file.write(result)

    def check_selected_or_not(self,element):
        element = driver.find_element(By.XPATH,element)
        if element.is_selected():
            return True

    def wait_and_find_and_click(self, element, locator_type):
        self.wait.until(EC.element_to_be_clickable((self.get_locator(locator_type), element))).click()

    def wait_and_find(self, element, locator_type):
        self.wait.until(EC.element_to_be_clickable((self.get_locator(locator_type), element)))
    
    def wait_till_element_located_click(self, element, locator_type):
        self.wait.until(EC.presence_of_element_located((self.get_locator(locator_type), element))).click()
    def wait_till_element_located(self, element, locator_type):
        self.wait.until(EC.presence_of_element_located((self.get_locator(locator_type), element)))
    def wait_until_presence_of_element_send_keys(self, element, value, locator_type):
        self.wait.until(EC.element_to_be_clickable((self.get_locator(locator_type), element))).send_keys(value)

    def wait_send_keys(self, element, value, locator_type):
        self.wait.until(EC.element_to_be_clickable((self.get_locator(locator_type), element))).send_keys(value)

    def get_text_in_a_list_for_given_list_locator(self, xpath_to_get_list_of_locators):
        list_to_get_list_of_locators = self.driver.find_elements(By.XPATH, xpath_to_get_list_of_locators)
        return [i.text for i in list_to_get_list_of_locators]
    
    def get_list_of_locators(self, xpath_to_get_list_of_locators):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_to_get_list_of_locators)))
        list_of_locators = self.driver.find_elements(By.XPATH, xpath_to_get_list_of_locators)
        return list_of_locators

    def get_text_for_a_element(self, locator):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        return self.driver.find_element(By.XPATH, locator).text

    def get_locator(self, locator_type):
        locators = {"id": By.ID, "xpath": By.XPATH}
        return locators[locator_type]
    
    def quit_driver(self):
        self.driver.quit()

    def is_element_present(self,locator_type,value,timeout=10):
        try:
            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((self.get_locator(locator_type), value))
            )
            return True
        except:
            return False
            
        
    def is_element_clickable(self,locator_type,value,timeout=10):
        try:
            WebDriverWait(driver, timeout).until(
                EC.element_located_to_be_selected((self.get_locator(locator_type), value))
            )
            return True
        except:
            return False
        
    def wait_for_alert(self):
        # Wait for the alert to be present
        alert = wait.until(EC.alert_is_present())
        return alert.text
    
    def get_text_soup(self):
        # Assume you have the HTML content as a string
        html_content = self.driver.page_source

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the table tag (modify as needed)
        table_tag = soup.find('table')

        # Extract text from the table tag
        table_text = table_tag.get_text(separator='\n', strip=True)

        table_text_list = table_text.splitlines()
        
        return str(table_text_list)
    
    def get_text_by_tag_or_xpath(self, tag_or_xpath):
        # Assume you have the HTML content as a string
        html_content = self.driver.page_source

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Check if the input is an XPath expression
        if tag_or_xpath.startswith('//') or tag_or_xpath.startswith('(//'):
            elements = soup.find_all(True, {'xpath': tag_or_xpath})
        else:
            # Find elements by tag name
            elements = soup.find_all(tag_or_xpath)

        # Extract text from the found elements
        text_content = '\n'.join(element.get_text(separator='\n', strip=True) for element in elements)

        return text_content
    

    def clear_field(self,locator_type,element):
        self.driver.find_element(self.get_locator(locator_type),element).clear()

    def return_dropdown_list(self):
        dropdown = self.driver.find_element(By.XPATH,testdata.status_filter_locator)
        dropdown_list = Select(dropdown)
        return dropdown_list
    
    def perform_sequence_of_actions(self,element,locator_type):
        # Locate the element to interact with
        element_to_interact = self.driver.find_element(self.get_locator(locator_type),element)

        # Create an ActionChains object
        actions = ActionChains(self.driver)

        # Perform a sequence of actions
        actions.move_to_element(element_to_interact).click().perform()
    
    def get_text_by_xpath(self,locator,type):
        element = self.driver.find_element(self.get_locator(type),locator)
        text = element.text
        return text
    
    def concatenate_counter(self,variable,counter):
        counter_variable  = f"{variable}_{counter}"
        return counter_variable
    
    def get_attribute(self,value,inputElement):
        text = inputElement.get_attribute(value)
        return text
    
    def login_rbac(self,mail,password):
        if basePage.is_element_present(self,"xpath",testdata.rbacEmailXpath):
            # Inputs the email id 
            basePage.wait_and_find_and_click(self,testdata.rbacEmailXpath,"xpath")
            basePage.wait_send_keys(self,testdata.rbacEmailXpath,mail,"xpath")
            time.sleep(3)
            # clicks on next button
            basePage.wait_and_find_and_click(self,testdata.nextBtnLocator,"xpath")
            time.sleep(3)
            # Inputs Password 
            basePage.wait_and_find_and_click(self,testdata.rbacPasswordXpath,"xpath")
            basePage.wait_send_keys(self,testdata.rbacPasswordXpath,password,"xpath")
            time.sleep(3)
            # click on sign_in
            basePage.wait_and_find_and_click(self,testdata.signInRbacBtn,"xpath")
            # Clicks on yes button in Stay signed in tab
            basePage.wait_and_find_and_click(self,testdata.yesBtnLocator,"xpath")

            time.sleep(5)
        else:
            pass

    def is_number(self,value):
        return self.isinstance(value, (int, float, complex))
    
    def countCheckedElements(self):
        elements = driver.find_elements(By.CSS_SELECTOR, "input:checked")
        return len(elements)
    
    def get_text_in_input_field(self,locator):
        input_field = driver.find_element(By.XPATH, testdata.enterRuleNameLocator)

        # Get the text from the input field
        text = input_field.get_attribute('value')
        return text

    
    def get_xpath_from_webelement(self, el, xpath: str = ""):
        if el.tag_name == "html":
            return "/html" + xpath
        
        str = el.tag_name
        parent = el.find_element("xpath", "..")
        children = parent.find_elements("xpath", "*")
        index = 0
        for child in children:
            if child.tag_name == el.tag_name:
                index += 1
                if child == el:
                    elem_index = index
        if index > 1:
            str += f"[{elem_index}]"
        str = "/" + str + xpath
        return self.get_xpath(el = parent, xpath = str)
    
    def select_option_by_index(self, select_element_id, index, type):
        """
        Clicks on an option in a <select> element identified by its ID.
        
        Args:
            driver: WebDriver instance
            select_element_id: ID of the <select> element
            index: Index of the option to click (0-based)
        """
        select_element = driver.find_element(self.get_locator(type),select_element_id)
        select = Select(select_element)
        select.select_by_index(index)

    def is_element_displayed(self, locator, type):
        element = driver.find_element(self.get_locator(type),locator)
        element.is_displayed()
        return True if element else False
    # def scroll_down(self, locator, type):
    def scroll_down(self):
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # element = driver.find_element(self.get_locator(type),locator)
        # driver.execute_script("arguments[0].scrollIntoView();", element)
        # driver.execute_script("window.scrollTo(0, 100)")
        # pag.press("pagedown")
        # pag.press("pagedown")
        # pag.press("pagedown")
        # pag.press("pagedown")
        self.driver.execute_script("window.scrollBy(0,100)")



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver,30)
o = basePage(driver, wait)