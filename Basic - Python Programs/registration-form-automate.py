from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('localhost:8000')

time.sleep(3)
elem = driver.find_element_by_id('FORM_ID')

elem.click()
time.sleep(5)

name = driver.find_element(By.XPATH, '//*[@id="name"]')
name.send_keys('NAME')

email = driver.find_element(By.XPATH, '//*[@id="email"]')
email.send_keys('EMAIL')


father_name = driver.find_element(By.XPATH,'//*[@id="f_name"]')
father_name.send_keys('FATHER_NAME')

jersey_size = driver.find_element(By.XPATH,'//*[@id="j_size"]')
jersey_size.send_keys('SIZE')

DOB = driver.find_element(By.XPATH,'//*[@id="dob"]')
DOB.send_keys('DOB')

phone_number = driver.find_element(By.XPATH,'//*[@id="number"]')
phone_number.send_keys('PHONE_NUMBER')

aadhar_number = driver.find_element(By.XPATH,'//*[@id="A_number"]')
aadhar_number.send_keys('ADDHAR_NUMBER')

image = driver.find_element(By.XPATH,'//*[@id="image"]')
# image.click()
image.send_keys('IMAGE_PATH')

sub = driver.find_element(By.XPATH, '/html/body/div[3]/form/div[8]/button')
sub.click()

time.sleep(3)
load = driver.find_element_by_tag_name('html')
load.send_keys(Keys.END)
