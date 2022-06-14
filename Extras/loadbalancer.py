import re
import subprocess as sub
import sys
import argparse

parser = argparse.ArgumentParser()


def main():
    parser.add_argument('host', help='Host to scan')

    args = parser.parse_args()

    return args.host


def execute(host):
    # change to use input on the string
    str = sub.run(f'lbd {host}', shell=True,
                  capture_output=True).stdout.decode('utf-8')
    final_str = re.findall(
        r'(?s).*', str, re.MULTILINE)

    final_str = final_str[0]

    final_str = final_str.replace(
        ': \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n', ': ')

    print('\n\n<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>', end='\n\n')
    print(final_str)
    print('<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>')


if __name__ == '__main__':
    args = main()
    execute(args)
