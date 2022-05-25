import re
import subprocess as sub
from terminal_colors import bcolors
from main import menu
import sys

if sys.platform == "linux" or sys.platform == "linux2":
    path = r'/home/manuel/Info-Program/Info-Gathering-Program/Trabalho'
elif sys.platform == "win32":
    path = r'C:\Users\mnlta\OneDrive\Documentos\GitHub\Info-Gathering-Programs\Trabalho'

sys.path.append(path)


class nmap:

    def __init__(self):
        self.host = []
        self.flags = []

    def concatenate_command(self):
        command = 'nmap'

    def check_options(self):
        print("Hosts: ", self.host)
        print('Flags: ', self.flags)
        pass


nmap_command = nmap()


def main():
    print('\n1. Target specification')
    print('2. Host discovery')
    print('3. Check options')
    print('3. Go Back!')
    choice = input(bcolors.UNDERLINE +
                   "\nInfo Gathering/Nmap" + bcolors.ENDC + " > ")

    if choice == '1':
        target_specificaion()
    elif choice == '2':
        host_discovery()
    elif choice == '3':
        nmap_command.check_options()
    elif choice == '4':
        menu()


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


def target_specificaion():
    print('\n1. Only one host')
    print('2. Custom list of hosts')
    print('3. Go Back!')
    choice = input(bcolors.UNDERLINE + "\nInfo Gathering/Nmap/Target_Specification" +
                   bcolors.ENDC + " > ")

    if choice == '1':
        print("\n1. To go back!")
        host = input(bcolors.UNDERLINE + "\nInfo Gathering/Nmap/Target_Specification/Host" +
                     bcolors.ENDC + " > ")
        if host != '1':
            nmap_command.host.append(host)
        target_specificaion()
    elif choice == '2':
        print(bcolors.WARNING +
              "\nWrite full path of the file if not in the same directory as the file!" + bcolors.ENDC)
        host = input(bcolors.UNDERLINE + "Info Gathering/Nmap/Target_Specification/Host" +
                     bcolors.ENDC + " > ")
        l = sub.run(f'locate {host}', shell=True,
                    capture_output=True).stdout.decode('utf-8')
        print(l)
        nmap_command.host.append(l)
    elif choice == '3':
        main()


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
    elif choice == '5':
        target_specificaion()


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
