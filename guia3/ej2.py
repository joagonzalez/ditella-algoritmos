import sys

def prod(m, n):
    return m * n

def pot(m, n):
    result = m

    if n == 0:
        result = 1
    elif n == 1:
        result = m
    else:
        for i in range(1,n):
            result = result * m
    
    return result

m = int(sys.argv[1])
n = int(sys.argv[2])

print("prod: " + str(prod(m, n)))
print("pot: " + str(pot(m, n)))

