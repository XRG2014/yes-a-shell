import sys
from colorama import Fore
 
n = len(sys.argv)

try:
    f = sys.argv[1]
    if n > 2 and f == "--help" or n > 2 and f == "--version":
        print(f'{Fore.LIGHTRED_EX}Error:{Fore.RESET} Invalid argument(s)')
        sys.exit()
    elif f == "--help":
        print("Usage: yes [STRING]...")
        print("  or:  yes OPTION")
        print("Repeatedly output a line with all specified STRING(s), or 'y'.")
        print("      --help        display this help and exit")
        print("      --version     output version information and exit")
        sys.exit()
    elif f == "--version":
        print("yes 2.x")
        print("Packaged by XRG2014 (2.x)")
        print("Written by XRG2014")
        sys.exit()
    elif f.startswith("-") and not f == "--version" and not f == "--help":
        print(f'{Fore.LIGHTRED_EX}Error:{Fore.RESET} Invalid argument(s)')
        sys.exit()
except IndexError:
    try:
        while True:
            print("y", end = " ")
            print()
    except KeyboardInterrupt:
        sys.exit()

try:
    while True:
        for i in range(1, n):
            print(sys.argv[i], end = " ")
        print()
except KeyboardInterrupt:
    sys.exit()
