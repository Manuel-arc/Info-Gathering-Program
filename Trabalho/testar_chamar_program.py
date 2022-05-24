import subprocess as sub
import re


def is_tool(name):
    """Check whether `name` is on PATH and marked as executable."""
    from shutil import which

    return which(name) is not None


def nmap_scan():
    nmap = sub.run('nmap 127.0.0.1', shell=True,
                   capture_output=True).stdout.decode('utf-8')

    # print(nmap)

    a = re.findall(
        r'\d{1,5}/\w{1,6}\s{1,9}\w{1,9}\s{1,9}\w{1,20}', nmap, re.MULTILINE)

    for e in a:
        print(e)

    c = []

    for port in a:
        c.append(re.match(r'\d{1,5}', port).group())

    for port in c:
        if port == '80':
            print("\nIt appears you have port 80 open!")
            res = input('Do you wanna do a gobuster? (y/n) ')
            print()
            if res.lower() == 'y':
                sub.run('gobuster dir -u 127.0.0.1 -w common.txt', shell=True)
            else:
                print('Ok, bye!')
                break


if __name__ == '__main__':
    print("1. Nmap scan")
    print("2. Gobuster scan")
    print("3. Teste de return_code")
    response = input("Escolha qual dos dois: ")

    if(response.lower() == '1'):
        a = is_tool('nmap')
        if a:
            nmap_scan()
    elif(response.lower() == '2'):
        a = is_tool('telnet')
        if not a:
            res = input(
                "Não foi encontrado o programa telnet, deseja instalar? (y/n) ")
            if res.lower() == 'y':
                print("Instalando...\n")
                try:
                    sub.run("sudo apt install telnet", shell=True)
                except:
                    print("Não foi possível instalar o programa")
                    exit()
                print("Instalado com sucesso!")
            else:
                print("\nSaindo...")
                exit()
    elif (response.lower() == '3'):
        nmap = sub.run('nmap 127.0.0.1', shell=True, capture_output=True)
        print(nmap.returncode)
    else:
        quit()
