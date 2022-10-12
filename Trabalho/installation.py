# /usr/bin/python3

linux_path = "path/to/install/tools"

linux_tools = ['nmap', 'gobuster',
               'locate', 'enum4linux']


def is_tool(name):
    """Check whether `name` is on PATH and marked as executable."""
    from shutil import which

    return which(name) is not None


def install_tools(tool_name):
    """Install the program if it is not installed."""
    import subprocess as sub
    print(f"Installing {tool_name}...")
    try:
        sub.run(f"sudo apt install {tool_name}", shell=True)
    except:
        print("Not possible to install the program")


for t in linux_tools:
    if not is_tool(t):
        install_tools(t)
