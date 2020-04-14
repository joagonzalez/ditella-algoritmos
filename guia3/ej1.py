import sys
import math

def raiz(num):
    return int(math.sqrt(num))

num = sys.argv[1:]

for n in num:
    print(raiz(int(n)))

