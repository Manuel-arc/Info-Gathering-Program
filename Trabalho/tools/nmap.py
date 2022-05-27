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

    def __init__(self):
        self.host = ''
        self.flags = []

    def concatenate_command(self):
        command = 'nmap'

    def check_options(self):
        print("Hosts: ", self.host)
        print('Flags: ', self.flags)


nmap_command = nmap()


def main():

    print('1. Help')
    print('2. Go Back!')
    choice = input(bcolors.UNDERLINE +
                   "\nInfo Gathering/Nmap" + bcolors.ENDC + " > ")

    choice = choice.split(" ")

    if choice[0].upper() == 'OPTIONS':
        nmap_command.check_options()
        print()
        main()
    elif choice[0].upper() == 'HOST':
        if choice[1].upper() == 'LIST':
            check_target_list(choice[2])
        else:
            nmap_command.host = choice[1]
        print()
        main()
    elif choice[0].upper() == 'FLAG':
        print('Choose your flags for the scan')
        print()
        main()
    elif choice[0] == '1':
        print("Type OPTIONS to see the host and flags for the scan.")
        print("Type HOST to choose a target.")
        print("Type HOST LIST to choose a list of targets.")
        print('Type FLAG to choose the flags for the scan.')
        print('Separate the flags with a space.')
        print()
        main()
    elif choice[0] == '2':
        main.menu()
    else:
        print("Incorrect input! Please try again!\n")
        main()


def nmap_scan():
    ip = input("Write the ip: ")
    nmap = sub.run(f'nmap {ip}', shell=True,
                   capture_output=True).stdout.decode('utf-8')

    if nmap.returncode == 0:
        a = re.findall(
            r'\d{1,5}/\w{1,6}\s{1,9}\w{1,9}\s{1,9}\w{1,20}', nmap, re.MULTILINE)

        for e in a:
            print(e)

        c = []

        for port in a:
            c.append(re.match(r'\d{1,5}', port).group())

        # to use gobuster next
        for port in c:
            if port == '80':
                print("\nIt appears you have port 80 open!")
                res = input('Do you wanna do a gobuster? (y/n) ')
                print()
                if res.lower() == 'y':
                    sub.run('gobuster dir -u 127.0.0.1 -w common.txt', shell=True)
                else:
                    print('Ok, bye!')
                    break
    else:
        print("Something went wrong! Sorry!")


def check_target_list(target_list):
    l = sub.run(f'locate {target_list}', shell=True,
                capture_output=True).stdout.decode('utf-8')
    output = l.split('\n')
    output = output[:-1]

    if len(output) == 1:
        nmap_command.host = target_list
    else:
        print('Choose from the given lists your choice:\n')
        for i in range(len(output)):
            print(f'{i} - {output[i]}')

        choice = input('Number of list: ')
        if choice.isdigit():
            nmap_command.host = output[int(choice)]


def discover_ports():
    print('\n1. TCP SYN discovery')
    print('2. TCP ACK discovery')
    print('3. UDP discovery')
    print('4. SCTP discovery')
    print('5. Go Back!')
    choice = input(bcolors.UNDERLINE + "\nInfo Gathering/Nmap/Host_Discovery/Discover_ports" +
                   bcolors.ENDC + " > ")

    if choice == '1':
        print('worked')
        nmap_command.flags.append('-PS')
    elif choice == '2':
        nmap_command.flags.append('-PA')
    elif choice == '3':
        nmap_command.flags.append('-PU')
    elif choice == '4':
        nmap_command.flags.append('-PY')


def host_discovery():

    print('\n1. List scan - simply list targets to scan')
    print('2. Ping scan - disable port scan')
    print('3. Treat all hosts as online')
    print('4. Discorver ports: (choose to get more options)')
    print('5. Exclude a list from a file')
    print('6. Go Back!')
    choice = input(bcolors.UNDERLINE + "\nInfo Gathering/Nmap/Host_Discovery" +
                   bcolors.ENDC + " > ")

    if choice == '4':
        discover_ports()
        for i in nmap_command.flags:
            print(i)


def call_gobuster():
    return 0
