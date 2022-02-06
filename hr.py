# Used to import the webdriver from selenium
from selenium import webdriver 
import os
import time
 
# Get the path of chromedriver which you have install
 
def startBot(username, password, url):
    path = "C:\\Users\\91733\\Desktop\\networkbooster\\chromedriver_win32\\chromedriver"
     
    # giving the path of chromedriver to selenium webdriver
    driver = webdriver.Chrome(path)
     
    # opening the website  in chrome.
    driver.get(url)
     
    # find the id or name or class of
    # username by inspecting on username input
    driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[5]/div[1]/div[1]/form/fieldset/label[2]/span[1]/input").send_keys(username)
     
    # find the password by inspecting on password input
    driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[5]/div[1]/div[1]/form/fieldset/label[3]/span[1]/input").send_keys(password)

     
    # click on submit
    driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[5]/div[1]/div[1]/form/fieldset/button/span").click()
    time.sleep(5)
    
    # Punch In Code 
    driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/button").click()
    time.sleep(5)
    # Punch Out Code

# Driver Code
# Enter below your login credentials
username = "s1073"
password = "prasanna@123@456"
 
# URL of the login page of site
# which you want to automate login.
url = "https://sbnasoftware.crystalhr.com"
 
# Call the function
startBot(username, password, url)
