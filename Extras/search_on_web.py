import selenium.webdriver as webdriver
from selenium.webdriver.firefox.options import Options
import time
from sys import platform
import subprocess as sub

linux_driver_path = '../Extras/Drivers/Linux/'

if platform == 'linux' or platform == 'linux2':
    options = Options()
    options.headless = True
    driver = webdriver.Firefox()
elif platform == 'win32':
    driver = webdriver.Chrome("Extras\Drivers\Windows\chromedriver.exe")


driver.get("https://www.google.com/")


def launch():

    time.sleep(100)


launch()
