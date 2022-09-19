# /usr/bin/python3

from art_logo import *
from terminal_colors import bcolors
# importar de outra pasta os scripts
from tools import nmap, gobuster, loadbalancer, dns_dumspter, js_css_files, enum4linux, waf
import subprocess as sub


def menu():
    print(bcolors.OKBLUE)
    print("1. Nmap scan")
    print("2. Gobuster scan")
    print("3. Whois scan")
    print("4. Loadbalancer scan")
    print("5. DNS dumpster")
    print('6. WAF')
    print('7. CSS and JS files')
    print("8. Enum4linux")
    print("9. Help")
    print("0. Exit")
    print(bcolors.ENDC)

    answer = input(bcolors.UNDERLINE + "\nInfo Gathering" +
                   bcolors.ENDC + " > ")

    _ = True

    while _:
        if answer.lower() == "1" or answer.lower() == 'nmap':
            nmap.main()
        elif answer.lower() == "2" or answer.lower() == 'gobuster':
            gobuster.main()
        elif answer.lower() == "3" or answer.lower() == 'whois':
            host = input("Host: ")
            str = sub.run(f'finalrecon --whois https://{host}', shell=True)
        elif answer.lower() == "4" or answer.lower() == 'loadbalancer':
            loadbalancer.main()
        elif answer.lower() == "5" or answer.lower() == 'dns dumspter":':
            dns_dumspter.main()
        elif answer.lower() == "6" or answer.lower() == 'waf':
            waf.scan_url()
        elif answer.lower() == "7" or answer.lower() == 'css' or answer.lower() == 'js':
            js_css_files.main()
        elif answer.lower() == "8" or answer.lower() == 'enum4linux':
            enum4linux.enum_scan()
        elif answer.lower() == "9" or answer.lower() == 'help':
            print(
                bcolors.OKCYAN + '\nYou can use the number or write the tool name to use it\n\n' + bcolors.ENDC)
            menu()
        elif answer.lower() == "0" or answer.lower() == 'exit':
            exit()
        else:
            print(bcolors.FAIL, bcolors.BOLD + "\nInvalid option. Plese try again!" +
                  bcolors.ENDC, end="\n\n")
            menu()

    exit()


def header():
    print(bcolors.HEADER)
    print(program_name, end="\n\n")
    print(version)
    print(author, bcolors.ENDC, end="\n\n")
    print("-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-", end='\n\n')


if __name__ == '__main__':
    header()

    menu()
