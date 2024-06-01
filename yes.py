import sys
 
n = len(sys.argv)

try:
    f = sys.argv[1]
except IndexError:
    sys.exit()

try:
    while True:
        for i in range(1, n):
            print(sys.argv[i], end = " ")
        print()
except KeyboardInterrupt:
    sys.exit()
