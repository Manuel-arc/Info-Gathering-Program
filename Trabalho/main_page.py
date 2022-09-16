# /usr/bin/python3

from art_logo import *
from terminal_colors import bcolors
# importar de outra pasta os scripts
from tools import nmap, finalrecon, gobuster, loadbalancer, testssl, dns_dumspter, js_css_files, enum4linux, waf


def menu():
    print(bcolors.OKBLUE)
    print("1. Nmap scan")
    print("2. Gobuster scan")
    print("3. Testssl scan")
    print("4. Finalrecon scan")
    print("5. Loadbalancer scan")
    print("6. DNS dumpster")
    print('7. WAF')
    print('8. CSS and JS files')
    print("9. Enum4linux")
    print("10. Help")
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
        elif answer.lower() == "3" or answer.lower() == 'testssl':
            testssl.main()
        elif answer.lower() == "4" or answer.lower() == 'finalrecon':
            finalrecon.main()
        elif answer.lower() == "5" or answer.lower() == 'loadbalancer':
            loadbalancer.main()
        elif answer.lower() == "6" or answer.lower() == 'dns dumspter":':
            dns_dumspter.main()
        elif answer.lower() == "7" or answer.lower() == 'waf':
            waf.scan_url()
        elif answer.lower() == "8" or answer.lower() == 'css' or answer.lower() == 'js':
            js_css_files.main()
        elif answer.lower() == "9" or answer.lower() == 'enum4linux':
            enum4linux.enum_scan()
        elif answer.lower() == "10" or answer.lower() == 'help':
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
