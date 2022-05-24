import subprocess as sub
import re


def nmap_scan(ip):
    nmap = sub.run(f'nmap {ip}', shell=True,
                   capture_output=True).stdout.decode('utf-8')

    if nmap.returncode == 0:
        a = re.findall(
            r'\d{1,5}/\w{1,6}\s{1,9}\w{1,9}\s{1,9}\w{1,20}', nmap, re.MULTILINE)

        for e in a:
            print(e)

        c = []

        for port in a:
            c.append(re.match(r'\d{1,5}', port).group())

        # to use gobuster next
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
    else:
        print("Something went wrong! Sorry!")


def flag_options():
    return 0


def call_gobuster():
    return 0
