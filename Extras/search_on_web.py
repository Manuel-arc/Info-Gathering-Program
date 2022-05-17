from sys import platform
import time
from unittest import result
import selenium.webdriver as webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager


linux_driver_path = '../Extras/Drivers/Linux/'

if platform == 'linux' or platform == 'linux2':
    driver = webdriver.Firefox()
elif platform == 'win32':
    #driver = webdriver.Chrome("Extras\Drivers\Windows\chromedriver.exe")
    driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get("https://www.startpage.com/")

search_term = 'dog'

search_box = driver.find_element_by_id('q')
search_box.send_keys(search_term)
search_box.submit()

links = driver.find_elements_by_class_name('result-link')

results = []
for link in links:
    href = link.get_attribute('href')
    print(href)
    results.append(href)

time.sleep(20)

driver.close()
