from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-notifications")
browser = webdriver.Chrome(options=chrome_options)
browser.get('http://www.google.com')

def search(info):
  search = browser.find_element_by_name('q')
  search.send_keys(info)
  search.send_keys(Keys.RETURN)
  time.sleep(5)
  browser.find_element_by_partial_link_text("Wikipedia").click()
  time.sleep(5)
  text = browser.find_element_by_tag_name("body").get_attribute("innerText")
  print(text)
  browser.quit()

