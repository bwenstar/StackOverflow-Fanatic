import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

SO_USERNAME = os.environ.get('SO_USERNAME')
SO_PASSWORD = os.environ.get('SO_PASSWORD')

opts = Options()
opts.headless = False
driver = webdriver.Firefox(options = opts)

try:
    driver.get('https://stackoverflow.com/users/login')
    driver.find_element_by_xpath('//input[@id="email"]').send_keys(SO_USERNAME)
    driver.find_element_by_xpath('//input[@id="password"]').send_keys(SO_PASSWORD)
    driver.find_element_by_xpath('//button[@id="submit-button"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//a[@class="my-profile js-gps-track"]').click()
    time.sleep(5)
except Exception as e:
    driver.quit()
    sys.exit("generic Selenium exception: " + str(e))

driver.quit()
sys.exit()

