import sys
 
n = len(sys.argv)

try:
    f = sys.argv[1]
    if f == "--help":
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
        print("yes: invalid option -- '" + f + "'")
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
