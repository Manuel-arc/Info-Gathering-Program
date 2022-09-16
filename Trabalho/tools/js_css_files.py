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


output_path = "/home/manuel/Documents/GitHub/Info-Gathering-Program/Trabalho/Output"


def main():
    print('1. Host to scan')
    print('2. List the files')
    print('3. Go back!')
    choice = input(bcolors.UNDERLINE +
                   "\nInfo Gathering/CSS_JS_files" + bcolors.ENDC + " > ")

    if choice == '1':
        host_to_scan()
    elif choice == '2':
        print("Write the host to which files you want to see")
        url = input("Host: ")
        list_url(url)
    elif choice == '3':
        print("Write the host to which files you want to see")
        url = input("Host: ")
        read_url(url)
    elif choice == '4':
        main_page.menu()
    else:
        print(bcolors.FAIL + "Invalid option!" + bcolors.ENDC)
        main()


def read_url(host):
    import re

    lines = []

    # check version in js files
    with open(f"{output_path}/{host}_javascript_files.txt", "r") as f:
        file_lines = f.readlines()
        lines = [line.rstrip() for line in file_lines]

    for line in lines:
        r = requests.get(line)
        found = re.findall(r'\w{0,20} v\d{0,3}.\d{0,3}.\d{0,3}', r.text)

        if not found:
            found = re.findall(
                r'\w{0,20} version \d{0,3}.\d{0,3}.\d{0,3}', r.text)

        if not found:
            found = re.findall(
                r'\w{0,20} \w{0,20} \w{0,20} \d{0,3}.\d{0,3}.\d{0,3}', r.text)

        if found:
            print(line + " > " + found[0])
        else:
            print(line + " > versão não encontrada")

    lines = []
    # check version in css files
    with open(f"{output_path}/{host}_css_files.txt", "r") as f:
        file_lines = f.readlines()
        lines = [line.rstrip() for line in file_lines]
    for line in lines:
        r = requests.get(line)
        found = re.findall(r'\w{0,20} v\d{0,3}.\d{0,3}.\d{0,3}', r.text)

        if not found:
            found = re.findall(
                r'\w{0,20} version \d{0,3}.\d{0,3}.\d{0,3}', r.text)

        if not found:
            found = re.findall(
                r'\w{0,20} \w{0,20} \w{0,20} \d{0,3}.\d{0,3}.\d{0,3}', r.text)

        if found:
            print(line + " > " + found[0])
        else:
            print(line + " > versão não encontrada")


def list_url(host):
    print('\n' + bcolors.BOLD + "Javascript files:" + bcolors.ENDC)
    with open(f"Output/{host}_javascript_files.txt", "r") as f:
        print(f.read())
    print()
    print(bcolors.BOLD + "CSS files:" + bcolors.ENDC)
    with open(f"Output/{host}_css_files.txt", "r") as f:
        print(f.read())


def host_to_scan():
    host = input('Host: ')

    url = f"https://{host}"

    session = requests.Session()

    session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'

    try:
        html = session.get(url).content
    except:
        print(bcolors.FAIL + "Invalid host!" + bcolors.ENDC)
        host_to_scan()

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
    with open(f"Output/{host}_javascript_files.txt", "w") as f:
        for js_file in script_files:
            print(js_file, file=f)

    with open(f"Output/{host}_css_files.txt", "w") as f:
        for css_file in css_files:
            print(css_file, file=f)

    choice = input(
        "Do you want to display the links with the found versions? (y/n)")
    if choice == 'y':
        read_url(host)
    else:
        print("If you want to see the results, open the files or use option 3!")
