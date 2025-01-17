from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep 
import os


def login():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-notifications")
    browser = webdriver.Chrome(options=chrome_options)
    browser.get('https://www.facebook.com/login.php?login_attempt=1&lwv=110')

    #this info is from a test user
    username = os.getenv("faceMail")
    password = os.getenv("facePassword")
    name = os.getenv("faceName")
    #enter username
    userName = browser.find_element_by_xpath("//input[@id='email' or @name='email']") 
    userName.send_keys(username)
    #enter password
    passWord = browser.find_element_by_xpath("//input[@id='pass']") 
    passWord.send_keys(password)
    #login
    logIn= browser.find_element_by_xpath("//button[@id='loginbutton']")
    logIn.click()
    sleep(5)
    print("login works")

def postingFace(post):
  browser.find_element_by_partial_link_text("Home").click()
  sleep(5)
  status= browser.find_element_by_xpath("//textarea[@name='xhpc_message']")
  status.send_keys(post);
  sleep(5)
  postIt = browser.find_element_by_xpath("//button[contains(.,'Post')]")
  postIt.click()
  sleep(5)
  browser.quit()

  






