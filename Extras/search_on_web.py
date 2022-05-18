from selenium.webdriver.chrome.options import Options as opt_Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from sys import platform
import time
import selenium.webdriver as webdriver 
import os

#stops webdriver installtion to print
os.environ['WDM_LOG'] = '0'

#install chrome driver to use search
def install_chrome_driver():
    return ChromeDriverManager().install()


options = opt_Chrome()
options.headless = True
driver = webdriver.Chrome(service=Service(install_chrome_driver()), options=options)

url = "https://www.startpage.com/"

driver.get(url)

search_term = 'dog'

search_box = driver.find_element_by_id('q')
search_box.send_keys(search_term)
search_box.submit()

#only works with startpage (for now. Need to se other browsers)
links = driver.find_elements_by_class_name('result-link')

results = []
#get the links, print and append to a list for later use
for link in links:
    href = link.get_attribute('href')
    print(href)
    results.append(href)


#close the driver
driver.close()
