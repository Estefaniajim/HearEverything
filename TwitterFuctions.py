from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep 
import os


chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-notifications")
browser = webdriver.Chrome(options=chrome_options)
browser.get("https://twitter.com/login")

#for twitter I didnt use a test account (sorry)
user = os.getenv("twitterAccount")
pas = os.getenv("twitterPassword")

def login():
  #username
  sleep(3)
  userName = browser.find_element_by_name("session[username_or_email]")
  userName.send_keys(user)
  #password
  password = browser.find_element_by_name("session[password]")
  password.send_keys(pas)
  #login
  sleep(3)
  signinButton = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div').click()
  
def tweet(comment):
  

