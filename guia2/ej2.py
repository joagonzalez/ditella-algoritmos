import sys

def par(num):
    if num % 2 == 0:
        return True
    else:
        return False

for i in range(int(sys.argv[1]) + 1):
    if par(i):
        print(str(i))