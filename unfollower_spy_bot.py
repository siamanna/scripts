from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

username = "username"
password = "password"

def __main__():

    driver = webdriver.Chrome(ChromeDriverManager.install())
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    time.sleep(10)
    return

__main___()
    
