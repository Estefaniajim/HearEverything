from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep 
import os



#for twitter I didnt use a test account (sorry)
user = os.getenv("twitterAccount")
pas = os.getenv("twitterPassword")

def login():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument("--disable-notifications")
  browser = webdriver.Chrome(options=chrome_options)
  browser.get("https://twitter.com/login")

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
  browser.quit()
  
def tweet(comment):
  into = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
  into.send_keys(comment)  
  tweet = browser.find_element_by_xpath("//span[@class='add-tweet-button ']//following-sibling::button[contains(@class,'tweet-action')]")
  tweet.click()