import re
import subprocess as sub
#from terminal_colors import bcolors
#import main_page
import sys
from os import listdir
from os.path import isfile, join

if sys.platform == "linux" or sys.platform == "linux2":
    path = r'/home/manuel/Info-Program/Info-Gathering-Program/Trabalho'
    wordlist_path = r'../Trabalho/Wordlists'
elif sys.platform == "win32":
    path = r'C:\Users\mnlta\OneDrive\Documentos\GitHub\Info-Gathering-Programs\Trabalho'
    wordlist_path = r'Trabalho\Wordlists'


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
    gobuster_scan()


def gobuster_scan(host=""):

    wordlist = [f for f in listdir(
        wordlist_path) if isfile(join(wordlist_path, f))]

    w = []

    for l in wordlist:
        d = sub.run(f'readlink -f {l}', shell=True,
                    text=True, capture_output=True)
        w.append(d.stdout.strip())

    if host == '':
        gobuster_command.host = input("Host: ")
    else:
        gobuster_command.host = host
    print('\nWordlists:')

    for i in range(len(wordlist)):
        print(str(i+1) + '. ' + wordlist[i])

    choice = input('Choice: ')
    gobuster_command.wordlist = wordlist[int(choice)-1]

    sub.run(
        f'gobuster dir -u {gobuster_command.host} -w {gobuster_command.wordlist[0]}', shell=True)
