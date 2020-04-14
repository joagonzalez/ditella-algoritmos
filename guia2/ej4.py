import sys

def factorial(n):
    result = 1
    for i in range(n):
        result = result * (n - i)

    return result 

def factorial_inv(n):
    result = 1
    for i in range(n):
        result = result * (1.0/(n - i))

    return result
def sumatoria(n):
    result = 0
    for i in range(n+1):
        result = result + i
    
    return result    

def sumatoria_inv(n):
    result = 0
    for i in range(n):
        result = result + 1/(i+1.0)
    
    return result    


n = int(sys.argv[1])

print("El factorial de " + str(n) + " es " + str(factorial(n)))
print("El factorial inverso de " + str(n) + " es " + str(factorial_inv(n)))
print("La suma de  los " + str(n) + " primeros numeros es " + str(sumatoria(n)))
print("La suma del inverso de los " + str(n) + " primeros numeros es " + str(sumatoria_inv(n)))
    