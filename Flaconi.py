from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import requests
import advertools as adv
import pandas as pd
from selenium.webdriver.common.by import By

""" a)Hover over MAKE-UP main nav menu """

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flaconi.de/")
makeup = driver.find_element(by=By.XPATH, value="//a[@href='/make-up/']")
ActionChains(driver).move_to_element(makeup).perform()

""" b)Check status code for all sub-links """

makeup = adv.sitemap_to_df('https://www.flaconi.de/sitemaps-de/sitemap_products_de-0.xml')
makeup.to_csv('makeup_categories.csv', index = False)
makeup = pd.read_csv('makeup_categories.csv')
makeup.head(5)
for url in makeup['loc']:
    status = requests.get(url)
    makeup['status'] = status.status_code
    print(f'Status code of {url} is {status.reason} and {status.status_code}')
driver.close()
