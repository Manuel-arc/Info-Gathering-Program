import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome("Extras\chromedriver.exe")
driver.get("https://www.google.com/")

def launch():
    
    time.sleep(100)


launch()
