import sys

n = int(sys.argv[1])

for i in range(n):
    msg = ''
    for j in range(i):
        msg = msg + '*'
    print(msg)