from webbrowser import Chrome
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(
    executable_path='G:\My Drive\DEV\Python\Web Scraper/chromedriver.exe')
driver.get('https://oxylabs.io/blog')
results = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

for element in soup.find_all(attrs="blog-card__content-wrapper"):
    name = element.find("h2")
    if name not in results:
        results.append(name.text)
print(results)
