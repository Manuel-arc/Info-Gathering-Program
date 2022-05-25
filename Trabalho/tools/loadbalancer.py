import re
import subprocess as sub
#from terminal_colors import bcolors
#from main import menu
import sys

if sys.platform == "linux" or sys.platform == "linux2":
    path = r'/home/manuel/Info-Program/Info-Gathering-Program/Trabalho'
elif sys.platform == "win32":
    path = r'C:\Users\mnlta\OneDrive\Documentos\GitHub\Info-Gathering-Programs\Trabalho'

sys.path.append(path)


class load_balancer:

    def __init__(self) -> None:
        pass


ldb_command = load_balancer()


def main():
    pass


def load_balancer_scan():
    str = sub.run('lbd 127.0.0.1', shell=True,
                  capture_output=True).stdout.decode('utf-8')
    final_str = re.findall(
        r'(?s).*', str, re.MULTILINE)

    final_str = final_str.replace('\n', ' ')
    final_str = final_str.replace('. ', '.\n')
    final_str = final_str.replace(') ', ')\n')
    final_str = final_str.replace(': ', ':\n')

    print(str)


load_balancer_scan()
