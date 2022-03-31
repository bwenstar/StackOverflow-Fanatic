import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

SO_USERNAME = os.environ.get('SO_USERNAME')
SO_PASSWORD = os.environ.get('SO_PASSWORD')

opts = Options()
opts.headless = True
driver = webdriver.Firefox(options = opts)

try:
    driver.get('https://stackoverflow.com/users/login')
    driver.find_element_by_xpath('//input[@id="email"]').send_keys(SO_USERNAME)
    driver.find_element_by_xpath('//input[@id="password"]').send_keys(SO_PASSWORD)
    driver.find_element_by_xpath('//button[@id="submit-button"]').click()
    time.sleep(2)
    #driver.find_element_by_xpath('//a[contains(@class,"my-profile")]').click()
    driver.find_element_by_xpath('//a[contains(@class,"s-user-card__small")]').click()
    time.sleep(5)
    driver.get('https://stackoverflow.com/users/logout')
    driver.find_element_by_xpath('//*[@id="content"]/div/form/div[2]/button').click()
    time.sleep(5)
except Exception as e:
    try: 
        driver.quit()
    except Exception as e:
        pass
    sys.exit("generic Selenium exception: " + str(e))

driver.quit()
sys.exit()
