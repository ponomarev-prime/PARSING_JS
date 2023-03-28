#
print('\nPARSER\n')

chromedriver_win32 = "chromedriver_win32\chromedriver.exe"
chromedriver_linux64 = "chromedriver_linux64\chromedriver"
url = "https://mail.ru/" 

import time 
 
import pandas as pd 
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager


# start by defining the options 
options = webdriver.ChromeOptions() 
options.page_load_strategy = 'none' 
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--log-level=3")


chrome_path = ChromeDriverManager().install() 
print(chrome_path)
chrome_service = Service(chrome_path) 
# pass the defined options and service objects to initialize the web driver 
driver = Chrome(options=options, service=chrome_service) 
driver.implicitly_wait(1)
 
driver.get(url) 
time.sleep(2)

content = driver.find_element(By.CSS_SELECTOR, "div[class*='grid_newscol ideback-16fnjrt'")

news = content.find_elements(By.TAG_NAME, "li")
#news = content.find_elements(By.CLASS_NAME, "news-item-container")

data_news = {}

for n in news:
    print(f't = {n.text}, h = {n.find_element(By.TAG_NAME, "a").get_attribute("href")}')
    if not n.text:
        print("text out")
        break
    
    data_news.update({n.text:n.find_element(By.TAG_NAME, "a").get_attribute("href")})
    #data_news.update({"link":n.find_element(By.TAG_NAME, "a").get_attribute("href")})

print(data_news)
print(len(data_news))



driver.close()
driver.quit()