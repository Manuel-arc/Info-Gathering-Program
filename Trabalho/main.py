from art_logo import program_name, version, author


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def menu():
    print(bcolors.OKBLUE + "1. Nmap scan")
    print("2. Gobuster scan")
    print("3. Testssl scan")
    print("4. theHarvester scan")
    print("5. Help")
    print("0. Exit" + bcolors.ENDC)

    answer = input(bcolors.UNDERLINE + "\nInfo Gathering" +
                   bcolors.ENDC + " > ")

    _ = True

    while _:
        if answer.lower() == "1" or answer.lower() == 'nmap':
            print('nmap')
            _ = False
        elif answer.lower() == "2" or answer.lower() == 'gobuster':
            print('gobuster')
            _ = False
        elif answer.lower() == "3" or answer.lower() == 'testssl':
            print('testssl')
            _ = False
        elif answer.lower() == "4" or answer.lower() == 'theharvester':
            print('theharvester')
            _ = False
        elif answer.lower() == "5" or answer.lower() == 'help':
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


if __name__ == '__main__':

    print(bcolors.HEADER)
    print(program_name)
    print()
    print(version)
    print(author, bcolors.ENDC, end="\n\n")
    print("-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-", end='\n\n')

    menu()
