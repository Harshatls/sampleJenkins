class testdata:
    # Po vendor credentials 
    # To be changed later
    # create access to all channels
    usernameFullAccess = 'tls.app@transformative.in'
    passwordFullAccess = 'Kuh9815598155'
    # view access 
    usernameAppTest1 = 'apptest1@transformative.in'
    passwordAppTest1 = 'Docu93789'
    # create access
    usernameAppTest2 = 'apptest2@transformative.in'
    passwordAppTest2 = 'Docu84932'


    # Locator to login to RBAC
    # Not changed in any project
    BROWSER = 'chrome'
    URL ='https://auth.tlslogistics.org/'
    rbacEmailXpath = "//input[@type='email'][@name='loginfmt']"
    rbacPasswordXpath = "//input[@type='password'][@name='passwd']"
    rbacLoginButton = "//button[normalize-space()='Login']"
    nextBtnLocator = "//input[@type='submit']"
    signInRbacBtn = "//input[@id='idSIButton9']"
    yesBtnLocator = "//input[@id='idSIButton9']"

    # 1 has only create access for com and india channels
    # 2 has create access for any europe channels 
    # tls.app has create access for both the channels

    # Auth locators
    requestAccessLocator = "//ul[@data-cy='settingsMenu']//div[@data-cy='requestAccessButton']"
    escalationRequestsLocator = "(//ul[@data-cy='settingsMenu']//div[@data-cy='escalateNotificationsButton'])[1]"
    grantAccessLocator = "//div[@data-cy='grantAccessButton']"
    pymetrikosuiRequestAccessLocator = "//table[@class='table']//a[@href='/settings/request-access/6']"
    # pymetrikosPermission = "//td[.='pymetrikosui']"
    pymetrikosRequestButton = "(//td[@class='w-64'])[7]//button"
    europeViewRequestButton = "(//td[@class='w-64'])[6]//button"
    europeCreateRequestButton = "(//td[@class='w-64'])[4]//button"
    # Grant access pymetrikos locators for app and view europe rules
    apptest1PymetrikosAppToggleLocator = "(//tr[contains(.,'pymetrikosui')]//input)[1]"
    apptest1PymetrikosEuropeToggleLocator = "(//tr[contains(.,'europe_fb_with_shopify_view')]//input)[1]"
    apptest1PymetrikosEuropeCreateToggleLocator = "(//tr[contains(.,'europe_fb_with_shopify_create')]//input)[1]"
    # Locators for grant related to apptest1@transformative requests
    apptest1RequestsLocatorsList = "(//tr[contains(.,'apptest1@transformative.in')])//button[contains(.,'Grant')]"
    apptest2RequestsLocatorsList = "(//tr[contains(.,'apptest2@transformative.in')])//button[contains(.,'Grant')]"
    # Pymetrikos locators
    createRuleLocator = "//button[@data-test='create-rule-button']" 
    editDeleteDuplicateLocators = "//div[@class='flex gap-2']"
    pymetrikosAppLocator = "//a[@href='https://auth.tlslogistics.org/pymetrikosui/dashboard']"
    pymetrikosChannelFilterLocator = "//select[contains(@class,'font-bold text-lg max-w-md')]"
    apptest1grantaccessLocator = "//p[contains(.,'apptest1@transformative.in')]"
    apptest2grantaccessLocator = "//p[contains(.,'apptest2@transformative.in')]"
    apptest1GrantAccessPymetrikosuiLocator = "//a[contains(.,'PYMETRIKOSUI')]"
    statusPymetrikosUiLocator = "(//button)[4]"
    createdAtLocator = "//th[.='Created At']"
    scrollElement = "//td[.='Buyer EU Last 5 days_Clicks']"
    statusToggleLocatorsList = "//input[@type='checkbox']"
    addConditionLocator = "//button[@data-test='add_condition_button']"
    ruleNameLocator = "//div[normalize-space()='Rule Name']"
    taskToPerformTextLocator = "//span[.='Task to perform: ']"
    forLastTextLocator = "//span[.='For Last:']"
    keywordsLocator = "//div[@data-test='keywords-title']"
    filterStringLocator = "//div[@class='font-sans text-base font-bold flex justify-between items-center']"
    addFilterStringButton = "//button[@data-test='filter_string_add_button']"
    selectFbAccountLocator = "//div[.='Select Fb Account(s)']"
    loggedInUserLocator = "//div[contains(text(),'Logged in user')]"
    createRuleButtonLocator = "//button[@data-test='submit_rule_button']"
    cancelButtonLocator = "//button[.='Cancel']"
    enterRuleNameLocator = "//input[@data-test='rule_name']"
    testRuleName = "testRule"
    # Task to perform dropdown locator 
    taskToPerformDropdownLocator = "(//select[@class='ml-4 select select-bordered'])[1]"
    pauseInDropDownLocator = "((//select[@class='ml-4 select select-bordered'])[1]//option)[1]"
    testCampaignInclude = "testCampaign"
    testAdsetInclude = "testAdset"
    testAdInclude = "testAd"
    campaignIncludeLocator = "//span//input[@name='Include_keywords_campaign']"
    adsetIncludeLocator = "//input[@name='Include_keywords_adset']"
    adIncludeKeyword = "//input[@name='Include_keywords_ad']"
    campaignExcludeLocator = "//input[@name='Exclude_keywords_campaign']"
    adsetExcludeLocator = "//input[@name='Exclude_keywords_adset']"
    adExcludeLocator = "//input[@name='Exclude_keywords_ad']"
    addedFilterStringLocator = "//span[normalize-space()='Filter String 2:']"
    removeFilterStringLocator = "//button[@type='button'][normalize-space()='X']"
    selectFbAccountDropdownLocator = "//div[@data-test='select-dropdown']"
    checkOneAccountLocator = "//input[@data-test='select-account-275828343342964']"
    loggedInUserTextLocator = "//div[@name='logged_in_user']"
    greaterThanErrorLocator = "//p[contains(.,'Greater Than Value must be a number')]"
    roasErrorLocator = "//p[.='Roas value must be a number']"
    ruleNameErrorLocator = "//p[.='Rule Name is required']"
    selectFbAccountsErrorLocator = "//p[.='Please select atleast one fb account']"
    letterForLast = "x"
    forLastInputLocator = "//input[@class='ml-2 input input-bordered w-24']"
    lastDaysMustBeANumberErrorLocator = "//p[.='Last days must be a number']"
    numberGreaterThanThirty = "31"
    errorLocatorMaxValue = "//p[.='Maximum value is 30']"
    minNumberAllowed = "-2222222222222222222222"
    errorLocatorMinValue = "//p[.='Cannot go beyond -1']"
    greaterThanFieldLocator = "//input[@data-test='greater_than_0']"
    greaterThanValue = "-1"
    greaterThanFieldErrorLocator = "//p[.='Greater Than Value cannot be negative']"
    lessThanRoasFieldLocator = "//input[@data-test='roi_0']"
    lessThanRoasNegativeValue = "-2"
    roasNegativeErrorLocator = "//p[.='ROAS Value cannot be negative']"
    europeChannelFilterLocator = "//option[.='EUROPE FB with Shopify']"
    goToConsoleLocator = "//button[.='Go to Console']"
    yourAppsLocator = "//h2[.='Your Apps']"
    searchBoxLocator = "//div[@class='p-4 shadow-md rounded-2xl flex items-center']"
    headerLocatorsList = "//thead[@class='bg-TableHeadingColor']//th"
    headersToBePresent = ['#', 'Status', 'Rule Name', 'Max Spend/Clicks', 'Rule Type', 'Min_roi', 'Created At', 'Created by', 'Edited At', 'Last Edited by', 'Options']
    dashboardSideBarLocator = "//div[@class='flex px-2 py-4 items-center gap-4 ']//div[@data-test='dashboard-button-label']"
    createARuleLocator = "//div[@class='flex px-2 py-4 items-center gap-4 ']//div[@data-test='create-rule-button-label']"
    shopifyChannelFilterLocator = "//select[@class='select select-bordered w-full  font-bold text-lg max-w-md']"

    # sample
    harshaProfileLocator = "//h5[.='Javvaji Harsha Vardhan']"
    docustackLocator = "//td[.='DOCUSTACK']"
    toggleListLocator = "(//input[@data-cy='toggleInput'])"