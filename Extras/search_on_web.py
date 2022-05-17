import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options
import time
from sys import platform
import subprocess as sub

if platform == 'linux' or platform == 'linux2':
    sub.run('export PATH=$PATH:~/Documents/Github/Info-Gathering-Program/Extras/Drivers/Linux/chromedriver', shell=True)
    driver = webdriver.Chrome()
elif platform == 'win32':
    driver = webdriver.Chrome("Extras\Drivers\Windows\chromedriver.exe")


driver.get("https://www.google.com/")


def launch():

    time.sleep(100)


launch()
