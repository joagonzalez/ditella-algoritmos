import sys

def factorial(n):
    result = 1
    for i in range(n):
        result = result * (n - i)
    return result 

def combinatorio(n, k):
    if n >= k:
        result = factorial(n) / (factorial(k) * factorial(n-k))
    else:
        result = None
    return result

n = int(sys.argv[1])
k = int(sys.argv[2])
i = int(sys.argv[3])

print('facotrial: ' + str(factorial(n)))
print('combinatorio: ' + str(combinatorio(n,k)))

for j in range(1,i):
    if j < n:
        print('combinatorio de ' + str(j) + ': ' + str(combinatorio(n,j)))
