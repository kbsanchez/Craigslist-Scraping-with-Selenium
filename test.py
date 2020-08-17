from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

driver = webdriver.Chrome()
driver.get('https://craigslist.com')
time.sleep(1)

element = driver.find_element_by_xpath('//*[@id="sss0"]/li[16]/a')
element.click()
time.sleep(2)


