# /usr/bin/python3

linux_path = "path/to/install/tools"

linux_tools = ['nmap', 'gobuster', 'testssl',
               'locate', 'finalrecon', 'lbd']


def is_tool(name):
    """Check whether `name` is on PATH and marked as executable."""
    from shutil import which

    return which(name) is not None


print(is_tool('lbd'))


def install_tools(tool_name):
    import subprocess as sub
    print(f"Instalando {tool_name}...")
    try:
        sub.run(f"sudo apt install {tool_name}", shell=True)
    except:
        print("Não foi possível instalar o programa")
