import re
import subprocess as sub
from terminal_colors import bcolors
import main_page
import sys
import os

if sys.platform == "linux" or sys.platform == "linux2":
    path = r''
elif sys.platform == "win32":
    path = r''

sys.path.append(path)


def main():
    print()
    print('1. Scan')
    print('2. Help')
    print('3. Go Back!')
    choice = input(bcolors.UNDERLINE +
                   "\nInfo Gathering/Enum4linux" + bcolors.ENDC + " > ")

    if choice == '1' or choice.lower() == 'scan':
        enum_scan()

    elif choice == '2' or choice.lower() == 'help':
        sub.run("enum4linux --help", shell=True)

        print("\n\n-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-", end='\n')

    elif choice == '3' or choice.lower() == 'exit':
        main_page.menu()

    else:
        print()
        print(bcolors.FAIL + "Invalid option!" + bcolors.ENDC)
        print()
        main()


def enum_scan(host='', write_file=False):

    write_path = ''

    dirname = os.path.dirname(write_path)

    if host == '':
        host = input("Host: ")

    if write_file:
        output = sub.run(f'enum4linux {host}',
                         shell=True, text=True, capture_output=True)
        filename = f'{dirname}/{host}_enum4linux.txt'
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as f:
            f.write(output.stdout)

        print('Scan finished and written in a file')
    else:
        enum_scan = f"enum4linux {host}"
        output = []
        p = sub.Popen(enum_scan, shell=True, stdout=sub.PIPE,
                      stderr=sub.STDOUT, cwd=None, text=True)
        while (True):
            next_line = p.stdout.readline()
            if next_line:
                output.append(str(next_line))
                print(next_line, end='')
            elif not p.poll():
                break
