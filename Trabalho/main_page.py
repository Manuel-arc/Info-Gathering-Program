# /usr/bin/python3

from art_logo import *
from terminal_colors import bcolors
# importar de outra pasta os scripts
from tools import nmap, commands, finalrecon, gobuster, loadbalancer, testssl, dns_dumspter


def menu():
    print(bcolors.OKBLUE)
    print("1. Nmap scan")
    print("2. Gobuster scan")
    print("3. Testssl scan")
    print("4. Finalrecon scan")
    print("5. Loadbalancer scan")
    print('8. Domain Map')
    print("7. Full scan")
    print("8. Help")
    print("0. Exit")
    print(bcolors.ENDC)

    answer = input(bcolors.UNDERLINE + "\nInfo Gathering" +
                   bcolors.ENDC + " > ")

    _ = True

    while _:
        if answer.lower() == "1" or answer.lower() == 'nmap':
            print('nmap')
            print(bcolors.UNDERLINE + "\nInfo Gathering/Nmap" +
                  bcolors.ENDC + " > ")
            nmap.main()
            _ = False
        elif answer.lower() == "2" or answer.lower() == 'gobuster':
            print('gobuster')
            print(bcolors.UNDERLINE + "\nInfo Gathering/Gobuster" +
                  bcolors.ENDC + " > ")
            gobuster.main()
            _ = False
        elif answer.lower() == "3" or answer.lower() == 'testssl':
            print('testssl')
            print(bcolors.UNDERLINE + "\nInfo Gathering/Testssl" +
                  bcolors.ENDC + " > ")
            testssl.main()
            _ = False
        elif answer.lower() == "4" or answer.lower() == 'finalrecon':
            print('finalrecon')
            print(bcolors.UNDERLINE + "\nInfo Gathering/Finalrecon" +
                  bcolors.ENDC + " > ")
            finalrecon.main()
            _ = False
        elif answer.lower() == "5" or answer.lower() == 'loadbalancer':
            loadbalancer.main()
        elif answer.lower() == "6" or answer.lower() == 'domain map':
            print('Domain Map')
        elif answer.lower() == "7" or answer.lower() == 'full':
            print('Do a fullscan!!')
        elif answer.lower() == "8" or answer.lower() == 'help':
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
