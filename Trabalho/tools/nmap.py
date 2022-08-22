from random import choices
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


class nmap:
    def __init__(self) -> None:
        self.flags = ""
        self.host = ""


nmap_commands = nmap()


def main():

    print('1. Help')
    print('2. Go Back!')
    nmap_commands.host = input(bcolors.UNDERLINE +
                               "\nInfo Gathering/Nmap" + bcolors.ENDC + " > Host: ")

    nmap_commands.flags = input(bcolors.UNDERLINE +
                                "\nInfo Gathering/Nmap" + bcolors.ENDC + " > Flags: ")

    nmap_scan(nmap_commands.host, nmap_commands.flags)


def nmap_scan(host, flags):
    nmap = sub.run(f'nmap {flags} {host}', shell=True,
                   capture_output=True).stdout.decode('utf-8')

    if nmap.returncode == 0:
        ''' a = re.findall(
            r'\d{1,5}/\w{1,6}\s{1,9}\w{1,9}\s{1,9}\w{1,20}', nmap, re.MULTILINE) '''

        print(nmap)

        if '80/tcp' in nmap or '443/tcp' in nmap:
            print("Port 80 or 443 is open!")
            choice = input("Do you want to run gobuster? (y/n)")
            if choice == 'y':
                call_gobuster()
        elif '139/tcp' in nmap or '445/tcp' in nmap:
            print("Port 139 or 445 is open!")
            choice = input("Do you want to run enum4linux? (y/n)")

    else:
        print("Something went wrong! Sorry!")


def call_gobuster():
    return 0
