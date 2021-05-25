
from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--incognito")

yv= input('Youtube Video Link: ')

driver = webdriver.Chrome(chrome_options=chrome_options)
while True:
        
    driver.get(yv)
    time.sleep(193)
