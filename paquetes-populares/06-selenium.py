from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

# options = webdriver.ChromeOptions()
# options.add_experimental_option('detach', True)
# browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://www.github.com')

link = browser.find_element(By.LINK_TEXT, "Sign in")
link.click()

user_input = browser.find_element(By.ID, "login_field")
pass_input = browser.find_element(By.ID, "password")
user_input.send_keys(os.environ.get('GH_USER'))
pass_input.send_keys(os.environ.get('GH_PASS'))
pass_input.send_keys(Keys.RETURN)

profile = browser.find_element(
    By.CLASS_NAME, "css-truncate.css-truncate-target.ml-1")

label = profile.get_attribute('innerHTML')
print(label)

assert "tu usuario" in label

browser.quit()