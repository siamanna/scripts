from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

username = "username"
password = "password"

def login(driver):
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("password").send_keys(u'\ue007')

def __main__():

    driver = webdriver.Chrome(ChromeDriverManager.install())
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    time.sleep(1)
    login()

    
    time.sleep(10000)


    return

__main___()
    
