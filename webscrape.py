from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import email, smtplib, ssl, getpass, io

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

chrome_options = Options()
chrome_options.add_argument("--headless")

class car:

    listing_date = ""
    listing_title = ""
    price = ""

    def description(self):
        desc_str = "Date posted: {0:10} \t {1: <30} \t Price: {2:10}\n".format(self.listing_date, self.listing_title, self.price)
        return desc_str


port = 465

# Create secure SSL context
context = ssl.create_default_context()

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

subject = f"Listings for {searchval} from Craigslist using Python"
body = f"Here are the ten most recent listings for {searchval} from Craigslist.\n\n"
sender_email = "devthrowaway741@gmail.com"
password = getpass.getpass(prompt="Enter developer account password: ")
receiver_email = input("Enter recipient email address: ")

# Creating a multipart message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

message.attach(MIMEText(body, "plain"))

fileName = "listings.txt"
f = open(fileName, "r")
attachment = MIMEText(f.read())
attachment.add_header('Content-Disposition', 'attachment', fileame=fileName)
message.attach(attachment)

signature = f"\n\nVisit github.com/kbsanchez for more cool projects!"

message.attach(MIMEText(signature, "plain"))

text = message.as_string()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
    

browser.quit()

