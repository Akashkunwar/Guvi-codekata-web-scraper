from selenium import webdriver
from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

WEBDRIVER = "C:\chromedriver\chromedriver.exe"

driver = Chrome(WEBDRIVER)

# driver.get("https://www.guvi.in/code-kata-main?concept=zen")
driver.get("https://www.guvi.in/sign-in?sourceUri=https%3A%2F%2Fwww.guvi.in%2Fcode-kata-main%3Fconcept%3Dzen")

# time.sleep(1)

email_input = driver.find_element(By.ID, "login_email")
email_input.send_keys("ID@gmail.com")

pass_input = driver.find_element(By.ID, "login_password")
pass_input.send_keys("Password")
pass_input.send_keys(Keys.RETURN)

time.sleep(1)

driver.get("https://www.guvi.in/code-kata")

time.sleep(3)

category_btns = driver.find_elements(By.CLASS_NAME, "btn-primary")

category_urls = []

for btn in category_btns:
    category_urls.append(str(btn.get_attribute('href')))

print(category_urls)