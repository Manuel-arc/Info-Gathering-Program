import re
import subprocess as sub
# from terminal_colors import bcolors
# import main_page
import sys
from os import listdir
from os.path import isfile, join

if sys.platform == "linux" or sys.platform == "linux2":
    path = r''
elif sys.platform == "win32":
    path = r''
    wordlist_path = r'Trabalho\Wordlists'


sys.path.append(path)


class gobuster:

    def __init__(self):
        self.host = []
        self.flags = []
        self.wordlist = ""
        self.wordlist_path = ''

    def concatenate_command(self):
        pass

    def check_options(self):
        print("Hosts: ", self.host)
        print('Flags: ', self.flags)


gobuster_command = gobuster()


def main():
    gobuster_scan()


def gobuster_scan(host=""):

    wordlist = [f for f in listdir(
        gobuster_command.wordlist_path)]

    if host == '':
        gobuster_command.host = input("Host: ")
    else:
        gobuster_command.host = host
    print('\nWordlists:')

    for i in range(len(wordlist)):
        print(str(i+1) + '. ' + wordlist[i])

    choice = input('Choice: ')
    gobuster_command.wordlist = gobuster_command.wordlist_path + \
        wordlist[int(choice)-1]

    sub.run(
        f'gobuster dir -u {gobuster_command.host} -w {gobuster_command.wordlist} {gobuster_command.flags}', shell=True)
