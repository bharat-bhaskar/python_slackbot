import selenium
import time
from selenium import webdriver

def update_facebook_status(status_text):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option(
        "prefs", {"profile.default_content_setting_values.notifications": 1}
    )
    driver = webdriver.Chrome(options=options)

    driver.maximize_window()

    driver.get("https://www.facebook.com/")

    time.sleep(2)
    email = driver.find_element("xpath","/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input")
    time.sleep(1)
    email.send_keys("extramailsofbharat@gmail.com")
    password = driver.find_element("xpath","/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input")
    time.sleep(2)
    password.send_keys("mummy1papa2didi3me4")
    login_btn = driver.find_element("xpath","/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")
    time.sleep(1)
    login_btn.click()
    time.sleep(5)
    status = driver.find_element("xpath","/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[2]")
    driver.execute_script("arguments[0].click();", status)
    time.sleep(3)
    status_tb = driver.switch_to.active_element
    status_tb.send_keys(status_text)
    time.sleep(2)
    post_btn = driver.find_element("xpath","/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div/div/div/div")
    print(post_btn)
    post_btn.click()
    time.sleep(2)
    driver.quit()

##
##update_facebook_status("This is a great day")
