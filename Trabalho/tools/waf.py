import re
import subprocess as sub
from terminal_colors import bcolors
import main_page
import sys
import os

if sys.platform == "linux" or sys.platform == "linux2":
    path = r''
elif sys.platform == "win32":
    path = r'o'

sys.path.append(path)


def scan_url(host=''):
    if host == '':
        host = input("Host: ")

    write_path = 't'

    dirname = os.path.dirname(write_path)

    error = f"ERROR:wafw00f:Something went wrong HTTPSConnectionPool(host='{host}', port=443)"

    result = sub.run(f'wafw00f https://{host}',
                     shell=True, capture_output=True, text=True)

    if error in result.stderr:
        result = sub.run(
            f'wafw00f http://{host}', shell=True, text=True)

    filename = f'{dirname}/{host}_wafw00f.txt'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        f.write(result.stdout)
