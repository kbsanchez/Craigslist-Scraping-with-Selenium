# Craigslist Data Extraction Using Selenium
### Created by Keylin Sanchez
#### This is a personal project I created to familiarize myself with Selenium and sending emails with Python. The program takes user input and sends an email to the specified recipient containing the ten most relevant listings for the search term entered by the user.
## General Setup
### Dependencies
#### This webscraper was written in (and requires) Python. You must install selenium and chromedriver.
### Install Selenium
#### Enter the following command in your working directory to install selenium: 
     pip install selenium
### Install chromedriver
#### Download chromedriver using [this link](https://chromedriver.chromium.org/downloads). Include the chromedriver location in your PATH environment variable.
### Developer email address
#### For the purposes of this project, I created a throwaway gmail account to send emails from.[^1][^2] If you wish to fork this repository, you will need to edit the email address used, because in order to run this program, it prompts you for the password to your account.
### Run the program
#### Enter the following command:
     python webscrape.py
## Running examples 
     % python webscrape.py
     % Enter search term: Honda Civic
     % Enter developer account password: 
     % Enter recipient email address: recipient@gmail.com
     % 

![Screen Shot 2022-03-17 at 1 09 34 AM](https://user-images.githubusercontent.com/66031870/158741337-626790e1-5c69-4ffc-8e72-b7f9556cae56.png)
![Screen Shot 2022-03-17 at 1 01 49 AM](https://user-images.githubusercontent.com/66031870/158740871-cbef0397-caf0-49a1-b141-39c0442a17ed.png)

[^1]: On May 30th, 2022, Google will be discontinuing its "Allow less secure apps" feature for gmail. This means that applications will no longer be able to access accounts using only a username and password. Google has [documentation](https://developers.google.com/gmail/api/quickstart/python) on how to how to gain access credentials using the OAuth2 authorization framework, and if this project were to be developed further in the future, that would be updated. For the purposes of this project, however, I chose to implement the current method.
[^2]: Resource used for learning how to [send emails with Python](https://realpython.com/python-send-email/#starting-a-secure-smtp-connection).
