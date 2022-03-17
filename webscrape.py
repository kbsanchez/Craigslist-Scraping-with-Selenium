from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import smtplib, ssl, getpass, io

chrome_options = Options()
chrome_options.add_argument("--headless")

class car:

    listing_date = ""
    listing_title = ""
    price = ""

    def description(self):
        desc_str = "Date posted: %-10s \t %-75s \t\t Price: $%-20s\n" % (self.listing_date, self.listing_title, self.price)
        return desc_str


browser = webdriver.Chrome(options=chrome_options)

# Navigates to craigslist
browser.get('http://craigslist.org')
assert 'craigslist' in browser.title

# Asks for user input
searchval = input("Enter search term: ")

# Enters search term
elem = browser.find_element(By.ID, 'query')
elem.send_keys(searchval, Keys.RETURN)

inFile = open("listings.txt", "w+")

carListings = [car() for i in range(1, 11)]
it = 1

for car in carListings:
    elem = browser.find_element(By.XPATH, '//*[@id="search-results"]/li[%s]/div/time' % it)
    car.listing_date = elem.text

    elem = browser.find_element(By.XPATH, '/html/body/section/form/div[4]/ul/li[%s]/div/h3/a' % it)
    car.listing_title = elem.text

    element = browser.find_element(By.XPATH, '/html/body/section/form/div[4]/ul/li[%s]/div/span[2]/span[1]' % it)
    car.price = element.text

    with io.open("listings.txt", "a+", encoding="utf-8") as f:
        f.write(car.description())

    it = it + 1

f.close()

browser.quit()

