import re
import subprocess as sub
from terminal_colors import bcolors
import main_page
import sys

if sys.platform == "linux" or sys.platform == "linux2":
    path = r'/home/manuel/Info-Program/Info-Gathering-Program/Trabalho'
elif sys.platform == "win32":
    path = r'C:\Users\mnlta\OneDrive\Documentos\GitHub\Info-Gathering-Programs\Trabalho'

sys.path.append(path)


def scan_url(host=''):
    if host == '':
        host = input("Host: ")

    error = f"ERROR:wafw00f:Something went wrong HTTPSConnectionPool(host='{host}', port=443)"

    result = sub.run(f'wafw00f https://{host}',
                     shell=True, capture_output=True, text=True)

    if error in result.stderr:
        result = sub.run(
            f'wafw00f http://{host}', shell=True, text=True)
