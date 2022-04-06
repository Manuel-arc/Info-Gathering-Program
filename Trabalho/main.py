import subprocess as sub
import re


def is_tool(name):
    """Check whether `name` is on PATH and marked as executable."""
    
    from shutil import which
    
    return which(name) is not None

def nmap_scan():
    nmap = sub.run('nmap 127.0.0.1', shell=True, capture_output=True).stdout.decode('utf-8')

    print(nmap)

    a = re.findall(r'\d{1,5}/\w{1,6}\s{1,9}\w{1,9}\s{1,9}\w{1,20}', nmap, re.MULTILINE)

    for e in a: print(e)

    c = []

    for port in a: 
        c.append(re.match(r'\d{1,5}', port).group())
        print(c)


print("1. Nmap scan")
print("2. Gobuster scan")
response = input("Escolha qual dos dois: ")

if(response.lower() == '1'):
    a = is_tool('nmap')
    print(a)
elif(response.lower() == '2'):
    a = is_tool('gobuster')
    print(a)
else:
    quit()

    
    
