import re
import subprocess as sub
from terminal_colors import bcolors
import main_page
import sys

if sys.platform == "linux" or sys.platform == "linux2":
    path = r''
elif sys.platform == "win32":
    path = r''

sys.path.append(path)


class load_balancer:

    def __init__(self) -> None:
        host = ''


ldb_command = load_balancer()


def main():
    print('\nMENU:')
    print('\n1. Load balancer scan')
    print('2. Go Back!')
    choice = input(bcolors.UNDERLINE +
                   "\nInfo Gathering/LoadBalancer" + bcolors.ENDC + " > ")

    if choice == '1':
        load_balancer_scan()
    elif choice == '2':
        main_page.menu()


def load_balancer_scan():

    ldb_command.host = input("\nHost: ")

    # change to use input on the string
    str = sub.run(f'lbd {ldb_command.host}', shell=True,
                  capture_output=True).stdout.decode('utf-8')
    final_str = re.findall(
        r'(?s).*', str, re.MULTILINE)

    final_str = final_str[0]

    final_str = final_str.replace(
        ': \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n', ': ')

    print('\n\n<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>', end='\n\n')
    print(final_str)
    print('<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>')
