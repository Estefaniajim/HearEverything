from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options 
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver.common.keys import Keys 
import time 
import os

chrome_options = webdriver.ChromeOptions() 
prefs = {"profile.default_content_setting_values.notifications": 2} 
chrome_options.add_experimental_option("prefs", prefs) 
browser = webdriver.Chrome("chromedriver.exe") 
browser.get('https://www.facebook.com/')

#this info is from a test user
username = os.getenv("faceMail")
password = os.getenv("facePassword")

def login():
  #enter username
  userName = browser.find_elements_by_xpath('//*[@id ="email"]') 
  userName[0].send_keys(username)
  #enter password
  passWord = browser.find_element_by_xpath('//*[@id ="pass"]') 
  passWord.send_keys(password)
  #login
  logIn= browser.find_elements_by_id('loginbutton') 
  logIn[0].click()
  print("login works")

def postingFace(post):
  status= browser.find_element_by_xpath("//textarea[@name='xhpc_message']")
  status.send_keys(post);
  postbutton = browser.find_element_by_xpath("//button[contains(.,'Post')]")
  postbutton.click()
  





