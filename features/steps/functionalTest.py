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

@then(u'click on PymetrikosUI app')
def step_impl(context):
    try:
        basepage.wait_and_find_and_click(testdata.pymetrikosAppLocator,"xpath")
    except:
        raise NotImplementedError(u'STEP: Then click on PymetrikosUI app')


@given(u'Count the number of rules that are both active and Inactive before sorting')
def step_impl(context):
    try:
        global count
        listOfLocatorsActiveNonActive = basepage.get_list_of_locators(testdata.statusToggleLocatorsList)
        count = len(listOfLocatorsActiveNonActive)
    except:
        raise NotImplementedError(u'STEP: Given Count the number of rules that are both active and Inactive before sorting')


@when(u'Click on the status toggle')
def step_impl(context):
    try:
        basepage.wait_and_find_and_click(testdata.statusPymetrikosUiLocator,"xpath")
        time.sleep(3)
    except:
        raise NotImplementedError(u'STEP: When Click on the status toggle')


@then(u'Count the number of rules that are in the list')
def step_impl(context):
    try:
        # After clicking on status toggle
        listOfActiveNonActive = basepage.get_list_of_locators(testdata.statusToggleLocatorsList)
        countAfterToggle = len(listOfActiveNonActive)
        activeRulesCount = basepage.countCheckedElements()
        if countAfterToggle == activeRulesCount:
            pass
        else:
            raise SystemExit("Status toggle is not functioning as expected")
        
    except:
        raise NotImplementedError(u'STEP: Then Count the number of rules that are in the list')

@given(u'Click on Create a rule')
def step_impl(context):
    try:
        basepage.wait_and_find_and_click(testdata.createRuleLocator,"xpath")
    except:
        raise NotImplementedError(u'STEP: Given Click on Create a rule')


@when(u'Check whether the form is opened or not')
def step_impl(context):
    try:
        if basepage.is_element_present("xpath",testdata.addConditionLocator):
            pass
        else:
            SystemExit("Create a rule is not opened when clicked on the create a rule link")
    except:
        raise NotImplementedError(u'STEP: When Check whether the form is opened or not')

@when(u'Check whether all the fields are present or not')
def step_impl(context):
    try:
        basepage.wait_and_find(testdata.ruleNameLocator,"xpath")
        ruleNameText = basepage.get_text_by_xpath(testdata.ruleNameLocator,"xpath")

        if ruleNameText == "Rule Name":
            pass
        else:
            raise SystemExit("Rule name field text is incorrect")
        taskToPerformText = basepage.get_text_by_xpath(testdata.taskToPerformTextLocator,"xpath")
        if taskToPerformText == "Task to perform:":
            pass
        else:
            raise SystemExit("Task to perform text is incorrect")
        forLastText = basepage.get_text_by_xpath(testdata.forLastTextLocator,"xpath")
        if forLastText == "For Last:":
            pass
        else:
            raise SystemExit("For last text is incorrect")
        if basepage.is_element_present("xpath",testdata.addConditionLocator):
            pass
        listKeywordsLocator = basepage.get_list_of_locators(testdata.keywordsLocator)
        if len(listKeywordsLocator) == 2:
            pass
        else:
            raise SystemExit("Keywords field not present")
        if basepage.is_element_present("xpath",testdata.filterStringLocator):
            pass
        else:
            raise SystemExit("Filter string field is not present")
        addFilterStringButton = basepage.get_text_by_xpath(testdata.addFilterStringButton,"xpath")
        if addFilterStringButton == "+ ADD FILTER STRING":
            pass
        else:
            raise SystemExit("Add filter string button not present")
        if basepage.is_element_present("xpath",testdata.selectFbAccountLocator):
            pass
        else:
            raise SystemExit("Select fb account dropdown not present")
        if basepage.is_element_present("xpath",testdata.loggedInUserLocator):
            pass
        else:
            raise SystemExit("Loggedin user field not present")
        basepage.wait_and_find(testdata.createRuleButtonLocator,"xpath")
        if basepage.is_element_present("xpath",testdata.createRuleButtonLocator):
            pass
        else:
            raise SystemExit("Create rule button not present")
        if basepage.is_element_present("xpath",testdata.cancelButtonLocator):
            pass
        else:
            raise SystemExit("Cancel button not present")
    except:
        raise NotImplementedError(u'STEP: When Check whether all the fields are present or not')
    
@when(u'Click on the input field to enter a new rule name')
def step_impl(context):
    try:
        basepage.wait_and_find_and_click(testdata.enterRuleNameLocator,"xpath")
    except:
        raise NotImplementedError(u'STEP: When Click on the input field to enter a new rule name')


@then(u'Type a rule name and check whether entered rule name is visible or not')
def step_impl(context):
    try:
        basepage.wait_send_keys(testdata.enterRuleNameLocator,testdata.testRuleName,"xpath")
        time.sleep(3)
        text = basepage.get_text_in_input_field(testdata.enterRuleNameLocator)
        if text == testdata.testRuleName:
            pass
        else:
            raise SystemExit("Entered name is not visible in the input field")

    except:
        raise NotImplementedError(u'STEP: Then Type a rule name and check whether entered rule name is visible or not')
    
@when(u'User clicks on task to perform dropdown and click on pause')
def step_impl(context):
    try:
        basepage.wait_and_find_and_click(testdata.taskToPerformDropdownLocator,"xpath")
        basepage.wait_and_find_and_click(testdata.pauseInDropDownLocator,"xpath")
    except:
        raise NotImplementedError(u'STEP: When User clicks on task to perform dropdown and click on pause')


@then(u'Check whether when selected pause only pause is visible')
def step_impl(context):
    try:
        text = basepage.get_text_by_xpath(testdata.pauseInDropDownLocator,"xpath")
        time.sleep(3)
        if text == 'Pause':
            pass
        else:
            raise SystemExit("When selected Pause , Other option is shown in the Task to perform field")
        
    except:
        raise NotImplementedError(u'STEP: Then Check whether when selected pause only pause is visible')
    
@when(u'Enter an Campaign in Include keywords section')
def step_impl(context):
    try:
        basepage.wait_send_keys(testdata.campaignIncludeLocator,testdata.testCampaignInclude,"xpath")
    except:
        raise NotImplementedError(u'STEP: When Enter an Campaign in Include keywords section')


@when(u'Enter an Adset in Include keywords section')
def step_impl(context):
    try:
        basepage.wait_send_keys(testdata.adsetIncludeLocator,testdata.testAdsetInclude,"xpath")
    except:
        raise NotImplementedError(u'STEP: When Enter an Adset in Include keywords section')


@when(u'Enter an Ad in Include keywords section')
def step_impl(context):
    try:
        basepage.wait_send_keys(testdata.adIncludeKeyword,testdata.testAdInclude,"xpath")
    except:
        raise NotImplementedError(u'STEP: When Enter an Ad in Include keywords section')


@then(u'Check whether the entered Include keywords are in the input fields or not')
def step_impl(context):
    try:
        campaignText = basepage.get_text_by_xpath(testdata.campaignIncludeLocator,"xpath")
        basepage.write_to_file(str(campaignText))
        adsetText = basepage.get_text_in_input_field(testdata.adsetIncludeLocator)
        adText = basepage.get_text_in_input_field(testdata.adIncludeKeyword)
        if campaignText == testdata.testCampaignInclude and adsetText == testdata.testAdsetInclude and adText == testdata.testAdInclude:
            pass
        else:
            raise SystemExit("Entered test details are not correctly shown in the input fields")
    except:
        raise NotImplementedError(u'STEP: Then Check whether the Include keywords are in the input fields or not')
    
@when(u'Enter an Campaign in Exclude keywords section')
def step_impl(context):
    try:
        basepage.wait_send_keys(testdata.campaignExcludeLocator,testdata.testCampaignInclude,"xpath")
    except:
        raise NotImplementedError(u'STEP: When Enter an Campaign in Exclude keywords section')


@when(u'Enter an Adset in Exclude keywords section')
def step_impl(context):
    try:
        basepage.wait_send_keys(testdata.adsetExcludeLocator,testdata.testAdsetInclude,"xpath")
    except:
        raise NotImplementedError(u'STEP: When Enter an Adset in Exclude keywords section')


@when(u'Enter an Ad in Exclude keywords section')
def step_impl(context):
    try:
        basepage.wait_send_keys(testdata.adExcludeLocator,testdata.testAdInclude,"xpath")
    except:
        raise NotImplementedError(u'STEP: When Enter an Ad in Exclude keywords section')


@then(u'Check whether the entered Exclude keywords are in the input fields or not')
def step_impl(context):
    try:
        campaignText = basepage.get_text_in_input_field(testdata.campaignExcludeLocator)
        adsetText = basepage.get_text_in_input_field(testdata.adsetExcludeLocator)
        adText = basepage.get_text_in_input_field(testdata.adsetExcludeLocator)
        basepage.write_to_file(str(campaignText))
        if campaignText == testdata.testCampaignInclude and adsetText == testdata.testAdsetInclude and adText == testdata.testAdInclude:
            pass
        else:
            raise SystemExit("Entered test details are not correctly shown in the input fields")
    except:
        raise NotImplementedError(u'STEP: Then Check whether the entered Exclude keywords are in the input fields or not')

@when(u'Click on Add filter string button')
def step_impl(context):
    try:
        basepage.wait_and_find_and_click(testdata.addFilterStringButton,"xpath")
    except:
        raise NotImplementedError(u'STEP: When Click on Add filter string button')


@then(u'Check whether the new filter string is added or not')
def step_impl(context):
    try:
        if basepage.is_element_present("xpath",testdata.addedFilterStringLocator):
            pass
        else:
            raise SystemExit("Add filter string button is not functioning as expected")
    except:
        raise NotImplementedError(u'STEP: Then Check whether the new filter string is added or not')

@when(u'Check for the remove filter string button')
def step_impl(context):
    try:
        if basepage.is_element_present("xpath",testdata.removeFilterStringLocator):
            raise SystemExit("Remove filter string button should not be present when there is only one Filter string")
        else:
            pass
    except:
        raise NotImplementedError(u'STEP: When Check for the remove filter string button')


@when(u'If not present click on the Add filter string')
def step_impl(context):
    try:
        basepage.wait_and_find(testdata.addFilterStringButton,"xpath")
        basepage.perform_sequence_of_actions(testdata.addFilterStringButton,"xpath")
        time.sleep(5)
    except:
        raise NotImplementedError(u'STEP: When If not present click on the Add filter string')


@then(u'Check for the remove filter string button')
def step_impl(context):
    try:
        if basepage.is_element_present("xpath",testdata.removeFilterStringLocator):
            pass
        else:
            raise SystemExit("Remove filter string button should be available when there are more than one filter strings")
    except:
        raise NotImplementedError(u'STEP: Then Check for the remove filter string button')
    
@when(u'Click on select fb account dropdown')
def step_impl(context):
    try:
        basepage.wait_and_find_and_click(testdata.selectFbAccountDropdownLocator,"xpath")
    except:
        raise NotImplementedError(u'STEP: When Click on select fb account dropdown')


@when(u'Select any account from the dropdown')
def step_impl(context):
    try:
        basepage.wait_and_find_and_click(testdata.checkOneAccountLocator,"xpath")
    except:
        raise NotImplementedError(u'STEP: When Select any account from the dropdown')


@then(u'Check selected account is shown in the field or not')
def step_impl(context):
    try:
        text = basepage.get_text_in_input_field(testdata.selectFbAccountDropdownLocator)
        basepage.write_to_file(str(text))
    except:
        raise NotImplementedError(u'STEP: Then Check selected account is shown in the field or not')

@when(u'Check whether the logged in user element is available or not')
def step_impl(context):
    try:
        basepage.wait_and_find(testdata.loggedInUserLocator,"xpath")
        if basepage.is_element_present("xpath",testdata.loggedInUserLocator):
            pass
        else:
            raise SystemExit("No field as Logged in user")
    except:
        raise NotImplementedError(u'STEP: When Check whether the logged in user element is available or not')


@then(u'Check whether the name shown in the field matches with the logged in user')
def step_impl(context):
    try:
        text = basepage.get_text_by_xpath(testdata.loggedInUserTextLocator,"xpath")
        if text in testdata.usernameFullAccess:
            pass
        else:
            raise SystemExit("Name in Logged in User field and User actually logged in are not same")
    except:
        raise NotImplementedError(u'STEP: Then Check whether the name shown in the field matches with the logged in user')
    
@when(u'Click on \'Create button\'')
def step_impl(context):
    try:
        basepage.wait_and_find_and_click(testdata.createRuleButtonLocator,"xpath")
    except:
        raise NotImplementedError(u'STEP: When Click on \'Create button\'')


@then(u'Check for the error on the page')
def step_impl(context):
    try:
        if basepage.is_element_present("xpath",testdata.greaterThanErrorLocator) and basepage.is_element_present("xpath",testdata.roasErrorLocator) and basepage.is_element_present("xpath",testdata.ruleNameErrorLocator) and basepage.is_element_present("xpath",testdata.selectFbAccountsErrorLocator):
            pass
        else:
            raise SystemExit("Errors are not shown for all mandatory fields")
    except:
        raise NotImplementedError(u'STEP: Then Check for the error on the page')
    
@when(u'Input a letter in the for last field')
def step_impl(context):
    try:
        basepage.wait_and_find(testdata.forLastInputLocator,"xpath")
        basepage.clear_field("xpath",testdata.forLastInputLocator)
        basepage.wait_send_keys(testdata.forLastInputLocator,testdata.letterForLast,"xpath")
        basepage.wait_and_find_and_click(testdata.createRuleButtonLocator,"xpath")
    except:
        raise NotImplementedError(u'STEP: When Input a letter in the for last field')


@when(u'Check for the error when entered letter')
def step_impl(context):
    try:
        time.sleep(3)
        if basepage.is_element_present("xpath",testdata.lastDaysMustBeANumberErrorLocator):
            pass
        else:
            raise SystemExit("Error is not shown when entered a letter in the for last field")
    except:
        raise NotImplementedError(u'STEP: When Check for the error when entered letter')


@when(u'Input a number greater than 30')
def step_impl(context):
    try:
        basepage.clear_field("xpath",testdata.forLastInputLocator)
        time.sleep(3)
        basepage.wait_send_keys(testdata.forLastInputLocator,testdata.numberGreaterThanThirty,"xpath")
        time.sleep(3)
    except:
        raise NotImplementedError(u'STEP: When Input a number greater than 30')


@when(u'Check for the error when entered number greater than 30')
def step_impl(context):
    try:
        if basepage.is_element_present("xpath",testdata.errorLocatorMaxValue):
            pass
        else:
            raise SystemExit("Error is not shown when number entered in for last field is greater than 30")
    except:
        raise NotImplementedError(u'STEP: When Check for the error when entered number greater than 30')


@when(u'Input a number less than -1')
def step_impl(context):
    try:
        basepage.clear_field("xpath",testdata.forLastInputLocator)
        basepage.wait_send_keys(testdata.forLastInputLocator,testdata.minNumberAllowed,"xpath")
        time.sleep(3)
    except:
        raise NotImplementedError(u'STEP: When Input a number less than -1')


@then(u'check for the error when entered number less than -1')
def step_impl(context):
    try:
        if basepage.is_element_present("xpath",testdata.errorLocatorMinValue):
            pass
        else:
            raise SystemExit("Error not shown when number entered less than -1 in for last field")
    except:
        raise NotImplementedError(u'STEP: Then check for the error when entered number less than -1')
    
@when(u'Input a number in the greater than field')
def step_impl(context):
    try:
        basepage.wait_and_find(testdata.greaterThanFieldLocator,"xpath")
        basepage.clear_field("xpath",testdata.greaterThanFieldLocator)
        basepage.wait_send_keys(testdata.greaterThanFieldLocator,testdata.greaterThanValue,"xpath")
        basepage.wait_and_find_and_click(testdata.createRuleButtonLocator,"xpath")
    except:
        raise NotImplementedError(u'STEP: When Input a number in the greater than field')

@then(u'Check whether the error is shown or not')
def step_impl(context):
    try:
        basepage.wait_and_find(testdata.greaterThanFieldErrorLocator,"xpath")
        time.sleep(3)
        if basepage.is_element_present("xpath",testdata.greaterThanFieldErrorLocator):
            pass
        else:
            raise SystemExit("Error not shown when entered a negative value")
    except:
        raise NotImplementedError(u'STEP: Then Check whether the error is shown or not')
    
@when(u'Input a number in the less than ROAS field')
def step_impl(context):
    try:
        basepage.wait_send_keys(testdata.lessThanRoasFieldLocator,testdata.lessThanRoasNegativeValue,"xpath")
        basepage.wait_and_find_and_click(testdata.createRuleButtonLocator,"xpath")
    except:
        raise NotImplementedError(u'STEP: When Input a number in the less than ROAS field')


@then(u'Check whether the ROAS error is shown or not')
def step_impl(context):
    try:
        if basepage.is_element_present("xpath",testdata.roasNegativeErrorLocator):
            pass
        else:
            raise SystemExit("Error not shown for ROAS ")
    except:
        raise NotImplementedError(u'STEP: Then Check whether the ROAS error is shown or not')
    
@when(u'Click on the cancel button')
def step_impl(context):
    try:
        basepage.wait_and_find_and_click(testdata.cancelButtonLocator,"xpath")
    except:
        raise NotImplementedError(u'STEP: When Click on the cancel button')


@then(u'Check whether the user is redirected back to PymetrikosUI home page or not')
def step_impl(context):
    try:
        time.sleep(4)
        if basepage.is_element_present("xpath",testdata.statusPymetrikosUiLocator):
            pass
        else:
            raise SystemExit("User not directed back to PymetrikosUI home page")
    except:
        raise NotImplementedError(u'STEP: Then Check whether the user is redirected back to PymetrikosUI home page or not')

@when(u'Click on channel filter and click on another channel')
def step_impl(context):
    try:
        time.sleep(10)
        basepage.wait_and_find(testdata.europeChannelFilterLocator,"xpath")
        basepage.select_option_by_index("//select[contains(@class,'font-bold text-lg max-w-md')]", 1, "xpath")
        time.sleep(3)
    except:
        raise NotImplementedError(u'STEP: When Click on channel filter and click on another channel')


@then(u'check whether the user is redirected back to dashboard page or not')
def step_impl(context):
    try:
        time.sleep(10)
        if basepage.is_element_present("xpath",testdata.createdAtLocator):
            pass
        else:
            raise SystemExit("User not redirected back to selected channel dashboard")
    except:
        raise NotImplementedError(u'STEP: Then check whether the user is redirected back to dashboard page or not')
    
@given(u'Scroll down the page')
def step_impl(context):
    try:
        time.sleep(10)
        # basepage.scroll_down(testdata.scrollElement,"xpath")
        # basepage.scroll_down()
        pyautogui.press("pagedown")
        time.sleep(10)
    except:
        raise NotImplementedError(u'STEP: Given Scroll down the page')


@then(u'Check whether user is still able to see the search bar or not')
def step_impl(context):
    try:
        pass
    except:
        raise NotImplementedError(u'STEP: Then Check whether user is still able to see the search bar or not')
    
