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


class final_recon:

    def __init__(self) -> None:
        pass

    def concatenate_command(self):
        pass

    def check_options(self):
        pass


final_recon_command = final_recon()


def main():
    pass


def whois():
    pass


def subdomain_enum():
    pass


def remove_with_regex():
    # Remove the first line of the output
    # comando is gonna be with input and not hardcoded
    str = sub.run('finalrecon --sub https://www.smasmaia.pt', shell=True,
                  capture_output=True).stdout.decode('utf-8')
    final_str = re.sub(
        r'[^a-z0-9]{29}', '', str)

    print(final_str)
