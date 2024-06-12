from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://www.facebook.com')

time.sleep(1)

username = driver.find_element(By.XPATH, '//*[@id="email"]')
EMAIL = "<YOUR_EMAIL>"
username.send_keys(EMAIL)

password = driver.find_element(By.XPATH, '//*[@id="pass"]')
PASSWORD= 'YOUR_PASSWORD'
password.send_keys(PASSWORD)

time.sleep(1)

login = driver.find_elements_by_tag_name('button')
for button in login:
    if button.text == 'Log In':
        button.click()
        time.sleep(4)

driver.refresh()

time.sleep(6)

status = driver.find_element(
    By.XPATH, '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span')

time.sleep(5)

status.click()

time.sleep(5)

text = driver.find_element(
    By.XPATH, '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div[1]/div/div[1]/div/div/div/div/div[2]/div/div/div/div')

POST = 'HEY EVERYONE!'
text.send_keys(POST)

post = driver.find_element(
    By.XPATH, '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div/div[1]')

post.click()
