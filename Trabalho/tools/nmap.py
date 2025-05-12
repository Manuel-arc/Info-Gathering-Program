from random import choices
import re
import subprocess as sub
from unittest import result
from terminal_colors import bcolors
import main_page
import sys
import concurrent.futures as cf
from tools import gobuster, enum4linux
import logging

if sys.platform == "linux" or sys.platform == "linux2":
    path = r''
elif sys.platform == "win32":
    path = r''

sys.path.append(path)


class nmap:
    def __init__(self) -> None:
        self.flags = ""
        self.host = ""

    def scan(self, host, flags, sudo=''):
        """ nmap = sub.run(f'{sudo} nmap {flags} {host}', shell=True,
                       capture_output=True, text=True) """
        nmap = f"{sudo} nmap {flags} {host}"
        output = []
        p = sub.Popen(nmap, shell=True, stdout=sub.PIPE,
                      stderr=sub.STDOUT, cwd=None, text=True)
        while (True):
            next_line = p.stdout.readline()
            if next_line:
                output.append(str(next_line))
                print(next_line, end='')
            elif not p.poll():
                break

        error = p.communicate()[1]

        return p.returncode, '\n'.join(output), error

        """ with sub.Popen(nmap, stdout=sub.PIPE, bufsize=1, universal_newlines=True) as p:
            for line in p.stdout:
                print(line, end='') """

        # return nmap.stdout, nmap.returncode


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

    thread_list = []

    result, data, _ = nmap_commands.scan(host, flags)
    # nmap_commands.scan(host, flags)

    if result != 0:
        result, data, _ = nmap_commands.scan(host, flags, 'sudo')

    elif result == 0:
        if "Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn" in data:
            flags += ' -Pn'
            data, result, _ = nmap_commands.scan(host, flags)

        if '80/tcp' in data or '443/tcp' in data:
            print("Port 80 or 443 is open!")
            choice = input("Do you want to run gobuster? (y/n)")
            if choice == 'y':
                thread_list.append('gobuster')

            choice = input("Do you want to see if it has a WAF? (y/n)")
            if choice == 'y':
                thread_list.append('waf')
        if '139/tcp' in data or '445/tcp' in data:
            print("Port 139 or 445 is open!")
            choice = input("Do you want to run enum4linux? (y/n)")
            if choice == 'y':
                thread_list.append('enum4linux')

        with cf.ThreadPoolExecutor(max_workers=2) as executor:
            executor.map(thread_function, thread_list)

    else:
        print("Something went wrong! Sorry!")


def call_gobuster(host):
    gobuster.gobuster_scan(host)


def call_enum(host):
    enum4linux.enum_scan(host, True)


def call_waf(host):
    pass


def thread_function(lista_programas):
    if lista_programas == 'gobuster':
        call_gobuster(nmap_commands.host)
    elif lista_programas == 'enum4linux':
        call_enum(nmap_commands.host)
    elif lista_programas == 'waf':
        call_waf(nmap_commands.host)
