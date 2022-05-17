from sys import platform

if platform == 'linux' or platform == 'linux2':
    print('Isto é linux')
elif platform == 'win32':
    print('Isto é windows')
