from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

def search(info):
  text = ""
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument("--disable-notifications")
  browser = webdriver.Chrome(options=chrome_options)
  browser.get('https://www.google.com/?gl=us&hl=en&pws=0&gws_rd=cr')
  try:
        # Wait for the search box to be available
        search_box = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'q'))
        )
        search_box.send_keys(info)
        search_box.send_keys(Keys.RETURN)

        # Wait for the Wikipedia link and click it
        wiki_link = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Wikipedia'))
        )
        wiki_link.click()

        # Wait for the page body to load
        page_body = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        page_container = browser.find_element(By.XPATH, '//*[@class="mw-page-container"]')
        elements = page_container.find_elements(by='css selector', value='p')
        count = 1
        for element in elements:
          tag_name = element.tag_name
          if count and tag_name == 'p':
            text += element.text
            text += ' '
            count -= 1
  finally:
    # Quit the browser
    browser.quit()
  return text