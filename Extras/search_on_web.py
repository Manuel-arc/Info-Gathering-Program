from selenium.webdriver.chrome.options import Options as opt_Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from sys import platform
import time
import selenium.webdriver as webdriver
import os

# stops webdriver installtion to print
os.environ['WDM_LOG'] = '0'

# install chrome driver to use search


def install_chrome_driver():
    return ChromeDriverManager().install()


options = opt_Chrome()
options.headless = True
driver = webdriver.Chrome(service=Service(
    install_chrome_driver()), options=options)

url = "https://www.smasmaia.pt/"

driver.get(url)

''' search_term = 'dog'

search_box = driver.find_element_by_id('q')
search_box.send_keys(search_term)
search_box.submit() '''

# only works with startpage (for now. Need to se other browsers)
#links = driver.find_elements_by_class_name('result-link')
links = driver.find_elements_by_tag_name('script')
links1 = driver.find_elements_by_tag_name('link')

results = []
# get the links, print and append to a list for later use
print("SCRIPT TAGS")
for link in links:
    #href = link.get_attribute('href')
    print(link.get_attribute('src'))
    # results.append(href)

print("LINK TAGS----------------------------------------------------")
for link in links1:
    #href = link.get_attribute('href')
    print(link.get_attribute('href'))
    # results.append(href)


# close the driver
driver.close()
