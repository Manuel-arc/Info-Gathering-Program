import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from terminal_colors import bcolors
import sys
import main_page

if sys.platform == "linux" or sys.platform == "linux2":
    path = r'/home/manuel/Info-Program/Info-Gathering-Program/Trabalho'
elif sys.platform == "win32":
    path = r'C:\Users\mnlta\OneDrive\Documentos\GitHub\Info-Gathering-Programs\Trabalho'


def main():
    print('1. Host to scan')
    print('2. Go back!')
    choice = input(bcolors.UNDERLINE +
                   "\nInfo Gathering/CSS_JS_files" + bcolors.ENDC + " > ")

    if choice == '1':
        host_to_scan()
    elif choice == '2':
        main_page.menu()
    else:
        print(bcolors.FAIL + "Invalid option!" + bcolors.ENDC)
        main()


def read_url(url):
    pass


def host_to_scan():
    host = input('Host: ')

    url = f"https://{host}"

    session = requests.Session()

    session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'

    html = session.get(url).content

    soup = bs(html, 'html.parser')

    script_files = []

    for script in soup.find_all('script'):
        if script.attrs.get("src"):
            script_url = urljoin(url, script.attrs.get("src"))
            script_files.append(script_url)

    css_files = []

    for css in soup.find_all('link'):
        if css.attrs.get("href"):
            css_url = urljoin(url, css.attrs.get("href"))
            css_files.append(css_url)

    print("Total script files in the page:", len(script_files))
    print("Total CSS files in the page:", len(css_files))

    # write file links into files
    with open("javascript_files.txt", "w") as f:
        for js_file in script_files:
            print(js_file, file=f)

    with open("css_files.txt", "w") as f:
        for css_file in css_files:
            print(css_file, file=f)
