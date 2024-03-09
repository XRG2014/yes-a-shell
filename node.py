import sys
import os
import time
try:
    from colorama import Fore
except ImportError:
    print("Installing Dependencies...")
    time.sleep(0.9)
    pkgs = "colorama"
    os.system(f'python3 -ubm pip install {pkgs}')
ver = "2.x"

n = len(sys.argv)

def ht():
    print("usage: node [--help] [--version] [--in-window] [--silent] [-hv?] [file]")
    print("-?, -h, --help:  display help text.")
    print("-v, --version:   display current version.")
    print("--in-window:     runs inside the main window (can change terminal appearance or behaviour; use with caution).")
    print("--silent:        do not print the result of the JavaScript execution.")

try:
    if sys.argv[1] == "-?" or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        if n >= 3:
            print(f'{Fore.LIGHTRED_EX}Error:{Fore.RESET} too many arguments.')
            ht()
            sys.exit()
        ht()
        sys.exit()
    elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
        if n >= 3:
            print(f'{Fore.LIGHTRED_EX}Error:{Fore.RESET} too many arguments.')
            ht()
            sys.exit()
        print(f'{ver} / LTS')
    elif sys.argv[1] == "--in-window":
        if not n >= 3:
            print(f'{Fore.LIGHTRED_EX}Error:{Fore.RESET} not enough arguments.')
            ht()
            sys.exit()
        for i in range(2, n):
            os.system(f'jsc {sys.argv[i]} --in-window')
    elif sys.argv[1] == "--silent":
        if not n >= 3:
            print(f'{Fore.LIGHTRED_EX}Error:{Fore.RESET} not enough arguments.')
            ht()
            sys.exit()
        for i in range(2, n):
            os.system(f'jsc {sys.argv[i]} --silent')
    else:
        for i in range(1, n):
            os.system(f'jsc {sys.argv[i]}')
except IndexError:
    ht()
    sys.exit()
