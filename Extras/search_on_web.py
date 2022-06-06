from urllib import response
import requests
from selenium.webdriver.chrome.options import Options as opt_Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from sys import platform
import time
import selenium.webdriver as webdriver
import os
import urllib.request

# stops webdriver installtion to print
os.environ['WDM_LOG'] = '0'

# install chrome driver to use search


def install_chrome_driver():
    return ChromeDriverManager().install()


# options to make the chrome GUI not pop up
options = opt_Chrome()
options.headless = True
driver = webdriver.Chrome(service=Service(
    install_chrome_driver()), options=options)

# url to make the search
url = "https://dnsdumpster.com"

driver.get(url)

# input the domain to search
search_term = 'cm-alenquer.pt'

search_box = driver.find_element_by_id('regularInput')
search_box.send_keys(search_term)
search_box.submit()

# find the search results by the class name
links = driver.find_elements_by_class_name('img-responsive')

if (len(links) == 1):
    print(links[0].get_attribute('src'))
    url = links[0].get_attribute('src')
    response = requests.get(url)
    search_term = search_term.split('.')[0]
    image = f"Images/{search_term}.png"
    urllib.request.urlretrieve(url, image)

else:
    for link in links:
        #href = link.get_attribute('href')
        print(link.get_attribute('src'))
        # results.append(href)

# close the driver
driver.close()
