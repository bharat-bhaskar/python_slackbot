import selenium
import time
from selenium import webdriver
import undetected_chromedriver as uc
def get_case_details():
    driver = uc.Chrome(use_subprocess=True)
    driver.maximize_window()
    driver.get("https://docs.google.com/spreadsheets/d/1dMWJV_QUFWBwT2xEo47jMkKgSlyq_MKxKSiO0Xk8oLI/edit#gid=0")
    time.sleep(3)
    url_chk = driver.current_url
    if "https://accounts.google.com/" in url_chk:
        print("Not logged in")
        print("Trying to log in now ... ")
        
        email = driver.find_element("xpath",'//*[@id="identifierId"]')
        time.sleep(1)
        email.send_keys("abcsolutions777@gmail.com")
        time.sleep(1)
        # Click Next button
        next_btn = driver.find_element("xpath",'/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button')
        next_btn.click()
        time.sleep(2)
        pwd = driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
        pwd.send_keys("abcdefgh@123")
        next_btn = driver.find_element("xpath",'/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button')
        next_btn.click()
        time.sleep(2)
    driver.get("https://docs.google.com/spreadsheets/d/1dMWJV_QUFWBwT2xEo47jMkKgSlyq_MKxKSiO0Xk8oLI/edit#gid=0")
    # case_num = driver.find_element("xpath","/html/body/div[4]/div/div[2]/div/div[5]/div[2]/div[1]/div[2]")
    time.sleep(2)
    # https://abcsolutions6.lightning.force.com/lightning/r/5005i00000QVbDwAAL/view
    # https://abcsolutions6.lightning.force.com/lightning/r/5005i00000QVb2DAAT/view

    driver.get("https://abcsolutions6.my.salesforce.com/")
    time.sleep(3)
    sf_email = driver.find_element("xpath","/html/body/div[1]/div[1]/div/div/div[2]/div[3]/form/div[1]/div/input[1]")
    print(sf_email)
    sf_email.send_keys("extramailsofbharat-udnn@force.com")
    time.sleep(2)
    sf_pwd = driver.find_element("xpath",'//*[@id="password"]')
    print(sf_pwd)
    sf_pwd.send_keys("abcdefgh123")
    time.sleep(1)
    sf_login_btn = driver.find_element("xpath",'//*[@id="Login"]')
    sf_login_btn.click()
    time.sleep(2)
    case_num = "1032"
    if case_num == "1032":
        print("case 1032")
        driver.get("https://abcsolutions6.lightning.force.com/lightning/r/5005i00000QVbDwAAL/view")
        time.sleep(5)
    if case_num == "1031":
        print("Case 1031")
        driver.get("https://abcsolutions6.lightning.force.com/lightning/r/5005i00000QVb2DAAT/view")
        time.sleep(3)
    
    email_tab = driver.find_element("xpath",'/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-case_-record_-page1___-case___-v-i-e-w/forcegenerated-flexipage_case_record_page1_case__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-three-col-template-desktop2/div/div/div/flexipage-record-home-scrollable-column[1]/slot/slot/flexipage-component2[3]/slot/flexipage-tabset2/div/lightning-tabset/div/slot/slot/flexipage-tab2[1]/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/div/div[1]/div/ul/li[2]')
    print(email_tab)
    time.sleep(2)
    driver.execute_script("arguments[0].click();", email_tab)
    time.sleep(1)
    # Compose email now
    # comp_email_btn = driver.find_element("xpath",'/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-case_-record_-page1___-case___-v-i-e-w/forcegenerated-flexipage_case_record_page1_case__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-three-col-template-desktop2/div/div/div/flexipage-record-home-scrollable-column[1]/slot/slot/flexipage-component2[3]/slot/flexipage-tabset2/div/lightning-tabset/div/slot/slot/flexipage-tab2[1]/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/div/div[1]/section/div/div[1]/button[2]/span')
    # comp_email_btn.click()
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    cmp_btn_xpath = '/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-case_-record_-page1___-case___-v-i-e-w/forcegenerated-flexipage_case_record_page1_case__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-three-col-template-desktop2/div/div/div/flexipage-record-home-scrollable-column[1]/slot/slot/flexipage-component2[3]/slot/flexipage-tabset2/div/lightning-tabset/div/slot/slot/flexipage-tab2[1]/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/div/div[1]/section/div/div[1]/button[2]'
    cmp_btn_css = '#\31 161\:0 > div > div.slds-grid.dummyControlsContainer > button.slds-button.slds-button--brand.testid__dummy-button-submit-action.slds-col.slds-no-space.dummyButtonSubmitAction.uiButton'
    comp_email_btn = WebDriverWait(driver, 200).until(EC.element_to_be_clickable((By.XPATH,cmp_btn_xpath)))
    print("Compose Button: ", comp_email_btn)
    action = ActionChains(driver)
    action.click(on_element=comp_email_btn).perform()
    insrt_tmplt_xpath = '/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-case_-record_-page1___-case___-v-i-e-w/forcegenerated-flexipage_case_record_page1_case__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-three-col-template-desktop2/div/div/div/flexipage-record-home-scrollable-column[1]/slot/slot/flexipage-component2[3]/slot/flexipage-tabset2/div/lightning-tabset/div/slot/slot/flexipage-tab2[1]/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/div/div[1]/section/div/div[3]/div/div/div[2]/div[1]/div/div[1]/div/ul/li[3]/div/div[1]/div/div/a/div/div'
    insert_template_icon = WebDriverWait(driver,200).until(EC.element_to_be_clickable((By.XPATH,insrt_tmplt_xpath)))
    cords = insert_template_icon.location_once_scrolled_into_view
    print(insert_template_icon,cords)

    action.click(on_element=insert_template_icon).perform()
    tmplt_sel_xpath = '/html/body/div[8]/div/ul/li[4]/a'
    tmplt_selctor = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,tmplt_sel_xpath)))
    action.click(on_element=tmplt_selctor).perform()
    send_btn_xpath = "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-case_-record_-page1___-case___-v-i-e-w/forcegenerated-flexipage_case_record_page1_case__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-three-col-template-desktop2/div/div/div/flexipage-record-home-scrollable-column[1]/slot/slot/flexipage-component2[3]/slot/flexipage-tabset2/div/lightning-tabset/div/slot/slot/flexipage-tab2[1]/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/div/div[1]/section/div/div[3]/div/div/div[2]/div[2]/button"
    send_btn = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,send_btn_xpath)))
    print("Send button : ", send_btn)
    action.click(on_element=send_btn).perform()


    time.sleep(20)

    driver.quit()


get_case_details()
   
