from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import io

class car:

    listing_desc = ""
    price = ""

    def description(self):
        desc_str = "%-75s \t\t Price: $%-20s" % (self.listing_desc, self.price)
        return desc_str


driver = webdriver.Chrome()
driver.get('https://craigslist.com')
time.sleep(1)

element = driver.find_element_by_xpath('//*[@id="sss0"]/li[16]/a')
element.click()
time.sleep(1)

element = driver.find_element_by_id('query')
element.send_keys('Honda Civic')
time.sleep(1)

element = driver.find_element_by_xpath('//*[@id="searchform"]/div[1]/button/span[1]')
element.click()
time.sleep(1)

txt_file = open("listings.txt", "w+")

j = 1
listt = [car() for i in range(1,11)]
for vehiclee in listt:

    element = driver.find_element_by_xpath('//*[@id="sortable-results"]/ul/li[%s]/p/a' % j)
    vehiclee.listing_desc = element.text
    time.sleep(1)

    element = driver.find_element_by_xpath('//*[@id="sortable-results"]/ul/li[%s]/p/span[2]/span[1]' % j)
    vehiclee.price = element.text
    time.sleep(1)

    #txt_file.write(listt[j-1].listing_desc)
    with io.open("listings.txt", "a+", encoding="utf-8") as f:
        f.write("%-75s \t\t Price: $%-20s \n" % (listt[j-1].listing_desc, listt[j-1].price))
        
    j = j+1

f.close()