# /usr/bin/python3

linux_path = "path/to/install/tools"

linux_tools = ['nmap', 'gobuster', 'testssl',
               'theHarvester', 'finalrecon', 'loadbalancer']


def is_tool(name):
    """Check whether `name` is on PATH and marked as executable."""
    from shutil import which

    return which(name) is not None


print(is_tool('finalrecon'))


def install_tools():
    import subprocess as sub
    print("Instalando telnet...")
    try:
        sub.run("sudo apt install telnet", shell=True)
    except:
        print("Não foi possível instalar o programa")
