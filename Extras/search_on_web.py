import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options
import time
from sys import platform
import subprocess as sub

linux_driver_path = '~/Documents/Github/Info-Gathering-Program/Extras/Drivers/Linux/'

if platform == 'linux' or platform == 'linux2':
    driver = webdriver.Firefox(f'{linux_driver_path}gechodriver')
elif platform == 'win32':
    driver = webdriver.Chrome("Extras\Drivers\Windows\chromedriver.exe")


driver.get("https://www.google.com/")


def launch():

    time.sleep(100)


launch()
