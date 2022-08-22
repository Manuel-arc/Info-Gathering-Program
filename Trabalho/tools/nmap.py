from random import choices
import re
import subprocess as sub
from unittest import result
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

    def scan(self, host, flags, sudo=''):
        nmap = sub.run(f'{sudo} nmap {flags} {host}', shell=True,
                       capture_output=True, text=True)

        return nmap.stdout, nmap.returncode


nmap_commands = nmap()


def main():
    print()
    print('1. Scan')
    print('2. Help')
    print('3. Go Back!')
    choice = input(bcolors.UNDERLINE +
                   "\nInfo Gathering/Nmap" + bcolors.ENDC + " > ")

    if choice == '1' or choice.lower() == 'scan':
        nmap_commands.host = input(bcolors.UNDERLINE +
                                   "\nInfo Gathering/Nmap/Scan" + bcolors.ENDC + " > Host: ")

        nmap_commands.flags = input(bcolors.UNDERLINE +
                                    "\nInfo Gathering/Nmap/Scan" + bcolors.ENDC + " > Flags: ")
        nmap_scan(nmap_commands.host, nmap_commands.flags)

    elif choice == '2' or choice.lower() == 'help':
        print()
        print("--help")
        print("man")
        help = input(bcolors.UNDERLINE +
                     "\nInfo Gathering/Nmap/Help" + bcolors.ENDC + " > ")

        if help.lower() == '--help':
            sub.run("nmap --help", shell=True)
        elif help.lower() == 'man':
            sub.run("man nmap", shell=True)
        else:
            print(bcolors.FAIL + "Invalid option!" + bcolors.ENDC)

        print("\n\n-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-", end='\n')

    elif choice == '3' or choice.lower() == 'exit':
        main_page.menu()

    else:
        print()
        print(bcolors.FAIL + "Invalid option!" + bcolors.ENDC)
        print()
        main()


def nmap_scan(host, flags):

    data, result = nmap_commands.scan(host, flags)

    if result != 0:
        data, result = nmap_commands.scan(host, flags, 'sudo')

    elif result == 0:
        print('\n'+data)

        if "Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn" in data:
            flags += ' -Pn'
            data, _ = nmap_commands.scan(host, flags)
            print(data)

        if '80/tcp' in data or '443/tcp' in data:
            print("Port 80 or 443 is open!")
            choice = input("Do you want to run gobuster? (y/n)")
            if choice == 'y':
                call_gobuster()
        elif '139/tcp' in data or '445/tcp' in data:
            print("Port 139 or 445 is open!")
            choice = input("Do you want to run enum4linux? (y/n)")

    else:
        print("Something went wrong! Sorry!")


def call_gobuster():
    return 0
