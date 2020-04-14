import sys

def invertir_string(palabra):
    palabra_inv = ""
    size = int(len(palabra))

    for i in range(size):
        palabra_inv += palabra[size-i-1]

    return palabra_inv

def comparar_string(palabra1, palabra2):
    result = False

    if palabra1 == palabra2:
        result = True
    
    return result

def palindromo(palabra):
    result = False
    size = int(len(palabra))
    
    if par(palabra):
        pos1 = palabra[:int(size/2)]
        pos2 = palabra[int(size/2):]

        print(pos1)
        print(pos2)

        print(invertir_string(pos2))
        # print(''.join(reversed(pos2)))

        if comparar_string(pos1, invertir_string(pos2)):
            result = True

        return result

    else:
        pos1 = palabra[:int(size/2)]
        pos2 = palabra[int(size/2)+1:]

        print(pos1)
        print(pos2)

        print(invertir_string(pos2))
        # print(''.join(reversed(pos2)))

        if comparar_string(pos1, invertir_string(pos2)):
            result = True
        
        return result

def par(palabra):
    result = False

    if len(palabra) % 2 == 0:
        result = True
    
    return result

# main

try:
    palabra = sys.argv[1]
except:
    print("Ingrese una palabra")
    exit

if palindromo(palabra):
    print("es palíndromo!")
else:
    print("no es palíndromo!")


