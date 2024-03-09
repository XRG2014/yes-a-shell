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

def ht():
    print("usage: nvm [--help] [--version] [-hv?] ...")
    print("-?, -h, --help:              display help text.")
    print("-v, --version, version:      display current set version of Node")
    print("ls-remote, version-remote:   list available Node releases / versions.")
    print("list:                        display all installed versions of Node.")
    print("ls:                          display all installed versions of Node with extra release info.")
    print("use, install:                set current version of Node.")
    print("alias:                       set Node version alias.")
    print("exec, run:                   run javascript program with Node.")
    print("which:                       display path to Node executable.")
def invalid():
    print(f'{Fore.LIGHTRED_EX}Error:{Fore.RESET} invalid argument.')
def invalid_v():
    print(f'{Fore.LIGHTRED_EX}Error:{Fore.RESET} invalid version.')
def invalid_p():
    print(f'{Fore.LIGHTRED_EX}Error:{Fore.RESET} invalid package.')
def invalid_a():
    print(f'{Fore.LIGHTRED_EX}Error:{Fore.RESET} invalid alias.')
def invalid_p():
    print(f'{Fore.LIGHTRED_EX}Error:{Fore.RESET} invalid package.')
def invalid_c():
    print(f'{Fore.LIGHTRED_EX}Error:{Fore.RESET} invalid command.')
def invalid_no():
    print(f'{Fore.LIGHTRED_EX}Error:{Fore.RESET} not enough arguments.')
def invalid_na():
    print(f'{Fore.LIGHTRED_EX}Error:{Fore.RESET} no alias specified.')
def invalid_nv():
    print(f'{Fore.LIGHTRED_EX}Error:{Fore.RESET} no version specified.')
def invalid_ta():
    print(f'{Fore.LIGHTRED_EX}Error:{Fore.RESET} too many arguments.')
def nvm_ls():
    print("Installed Node versions:")
    print(f'{ver} / LTS - Modified version of jsc command')

n = len(sys.argv)

node_path = "~/Documents/.nvm/bin/node.py"

try:
    f = sys.argv[1]
except IndexError:
    ht()
    sys.exit()

if f == "--version" or f == "-v" or f == "version":
    try:
        r = sys.argv[2]
    except IndexError as e:
        print(f'Current Node version: {ver} / LTS')
        sys.exit()
    if "e" not in locals():
        invalid_ta()
        ht()
    sys.exit()
elif f == "ls-remote" or f == "version-remote":
    try:
        r = sys.argv[2]
    except IndexError:
        r = ""
    if r.startswith("--lts=") and not r == "--lts=" or r == "--lts" or r.startswith("lts/") and not r == "lts/" or r == "":
        if n >= 3 and not r.startswith('--lts') and not r.startswith('lts/'):
            invalid()
            ht()
            sys.exit()
        elif n >= 4:
            invalid_ta()
            ht()
            sys.exit()
        print("Available Node releases / versions:")
        print(f'{ver} / LTS - Modified version of jsc command')
        sys.exit()
    else:
        invalid()
        ht()
    sys.exit()
elif f == "-h" or f == "--help" or f == "-?":
    if n >= 2:
        invalid_ta()
    ht()
    sys.exit()
elif f == "exec":
    try:
        r = sys.argv[2]
        if r == ver:
            if sys.argv[3] == "node":
                if not n >= 5:
                    os.system(f'python3 -ub {node_path} -h')
                    sys.exit()
                for i in range(4, n):
                    os.system(f'python3 -ub {node_path} {sys.argv[i]}')
                sys.exit()
            else:
                invalid()
                ht()
        elif r == "--lts" or r.startswith("--lts=") and not r == "--lts=" or r.startswith("lts/") and not r == "lts/":
            if not n >= 4:
                os.system(f'python3 -ub {node_path} -h')
                sys.exit()
            for i in range(3, n):
                os.system(f'python3 -ub {node_path} {sys.argv[i]}')
            sys.exit()
        else:
            invalid_v()
            ht()
    except IndexError:
        invalid_no()
        ht()
    sys.exit()
elif f == "which":
    try:
        r = sys.argv[2]
        if r == ver or r == "node" or r == "default":
            if n >= 4:
                invalid_ta()
                ht()
                sys.exit()
            print(node_path)
            sys.exit()
        else:
            invalid_v()
            ht()
    except IndexError:
        invalid_no()
        ht()
    sys.exit()
elif f == "alias":
    try:
        r = sys.argv[2]
        try:
            if r == "default" or r == "node":
                if sys.argv[3] == ver:
                    if n >= 5:
                        invalid_ta()
                        ht()
                        sys.exit()
                    sys.exit()
                else:
                    invalid_v()
                    ht()
            else:
                invalid_a()
                ht()
        except IndexError:
            invalid_nv()
            ht()
    except IndexError:
        invalid_na()
        ht()
    sys.exit()
elif f == "install":
    try:
        r = sys.argv[2]
        if r == "node" or r == ver or r == "--lts" or r.startswith('--lts=') and not r == "--lts=" or r.startswith('lts/') and not r == "lts/":
            if n >= 4:
                invalid_ta()
                ht()
                sys.exit()
        elif r == "-g" or r == "--global":
            print(f'{Fore.LIGHTRED_EX}Error:{Fore.RESET} global arguments are not supported')
            ht()
            sys.exit()
        else:
            invalid_p()
            ht()
        sys.exit()
    except IndexError:
        invalid_no()
        ht()
    sys.exit()
elif f == "use":
    try:
        r = sys.argv[2]
        if r == "default" or r == "node" or r == ver or r == "--lts" or r.startswith('--lts=') and not r == "--lts=" or r.startswith('lts/') and not r == "lts/":
            if n >= 4:
                invalid_ta()
                ht()
                sys.exit()
        else:
            invalid_p()
            ht()
        sys.exit()
    except IndexError:
        invalid_no()
        ht()
    sys.exit()
elif f == "run":
    try:
        r = sys.argv[2]
        if r == "node" or r.startswith('--lts=') and not r == "--lts=" or r.startswith('lts/') and not r == "lts/" or r == "--lts":
            if not n >= 3:
                invalid_no()
                ht()
                sys.exit()
            if not n >= 4:
                os.system(f'python3 -ub {node_path} -h')
                sys.exit()
            for i in range(3, n):
                os.system(f'python3 -ub {node_path} {sys.argv[i]}')
            sys.exit()
        else:
            invalid_c()
            ht()
    except IndexError:
        invalid_no()
        ht()
    sys.exit()
elif f == "list":
    def nvm_list():
        print("Installed Node verisons:")
        print(f'{ver} / LTS')
    try:
        r = sys.argv[2]
    except IndexError as e:
        nvm_ls()
        sys.exit()
    if "e" in locals():
        pass
    elif r == "node":
        if n >= 3 and not r == "node" or n >= 4:
            invalid_ta()
            ht()
            sys.exit()
        nvm_list()
        sys.exit()
    else:
        invalid()
        ht()
    sys.exit()
elif f == "ls":
    if n >= 3:
        invalid_ta()
        ht()
    else:
        nvm_ls()
    sys.exit()
else:
    invalid()
    ht()
    sys.exit()
