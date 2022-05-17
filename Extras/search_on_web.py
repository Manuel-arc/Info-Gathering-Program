import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options
import time
from sys import platform

if platform == 'linux' or platform == 'linux2':
    driver = webdriver.Chrome(executable_path="Extras\Drivers\chromedriver")
elif platform == 'win32':
    driver = webdriver.Chrome("Extras\Drivers\chromedriver.exe")


driver.get("https://www.google.com/")


def launch():

    time.sleep(100)


launch()
