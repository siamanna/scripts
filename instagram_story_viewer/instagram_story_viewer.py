from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from time import sleep
import sys
from igloginfo import username, pw

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()  # Ensure ChromeDriver is in your PATH
        self.driver.get("https://instagram.com")
        
        # Log in
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "username"))
        ).send_keys(username)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "password"))
        ).send_keys(pw)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        ).click()

        # Dismiss pop-ups
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
        ).click()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
            ).click()
        except TimeoutException:
            pass  # No second pop-up

        sleep(2)  # Allow the page to load
    
    def get_viewers(self, target_user):
        # Open your story
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Your Story']"))
        ).click()

        # Click viewers icon
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Story viewers']"))
            ).click()
        except TimeoutException:
            print("No viewers yet!")
            return
        
        # Scroll and search for the target user
        scroll_box = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='isgrP']"))
        )
        
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight; return arguments[0].scrollTop;",
                scroll_box,
            )
            sleep(1)
            
            # Get the list of usernames
            usernames = [
                user.text for user in scroll_box.find_elements(By.XPATH, "//div[@class='FPmhX notranslate MBL3Z']")
            ]
            if target_user in usernames:
                print(f"{target_user} has seen your story!")
                return
        
        print(f"{target_user} hasn't seen your story yet!")

# Main program
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python igstoryviewer.py <username>")
        sys.exit(1)
    
    target_user = sys.argv[1]
    bot = InstaBot(username, pw)
    bot.get_viewers(target_user)
