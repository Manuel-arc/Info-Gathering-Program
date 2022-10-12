from urllib import response, request
import requests
from selenium.webdriver.chrome.options import Options as opt_Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import selenium.webdriver as webdriver
import os
from sys import platform
import main_page


def main():
    print('1. Search domain map')
    print("2. Go back")
    choice = input("Enter your choice: ")

    if choice == '1':
        print("domain")
    elif choice == '2':
        main_page.menu()
    else:
        print("Invalid choice")
        main()


def install_chrome_driver():
    return ChromeDriverManager().install()


def domain_map_search():
    domain = input("Enter the domain: ")

    # stops webdriver installtion to print
    os.environ['WDM_LOG'] = '0'

    # install chrome driver to use search
    # options to make the chrome GUI not pop up
    options = opt_Chrome()
    options.headless = True
    driver = webdriver.Chrome(service=Service(
        install_chrome_driver()), options=options)

    # url to make the search
    url = "https://dnsdumpster.com"

    driver.get(url)

    # input the domain to search
    search_term = domain

    search_box = driver.find_element_by_id('regularInput')
    search_box.send_keys(search_term)
    search_box.submit()

    # find the search results by the class name
    links = driver.find_elements_by_class_name('img-responsive')

    if (len(links) == 1):
        url = links[0].get_attribute('src') 
        search_term = search_term.split('.')[0]
        image = ''
        if platform == 'linux' or platform == 'linux2':
            image = f"../Images/{search_term}.png"

        request.urlretrieve(url, image)
        print("Download complete!!!")

    else:
        for link in links:
            #href = link.get_attribute('href')
            print(link.get_attribute('src'))
            # results.append(href)

    # close the driver
    driver.close()
