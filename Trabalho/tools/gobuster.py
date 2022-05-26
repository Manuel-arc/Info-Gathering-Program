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


class gobuster:

    def __init__(self):
        self.host = []
        self.flags = []
        self.wordlist = []

    def concatenate_command(self):
        pass

    def check_options(self):
        print("Hosts: ", self.host)
        print('Flags: ', self.flags)


gobuster_command = gobuster()


def main():
    pass


def gobuster_scan():
    gobuster_command.host = input("Host: ")
    print('Wordlists:')
    print('1. common.txt')
    print('2. directories.txt')
    choice = input('Choice: ')
    if choice == '1':
        gobuster_command.wordlist.append('../Trabalho/Wordlists/common.txt')
    elif choice == '2':
        gobuster_command.wordlist.append(
            '../Trabalho/Wordlists/directories.txt')

    sub.run(
        f'gobuster dir -u {gobuster_command.host} -w {gobuster_command.wordlist[0]}', shell=True)
