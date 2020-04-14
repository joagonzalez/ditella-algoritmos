import sys

def contar(lista):
    letras = 0
    for palabra in lista:
        for letra in palabra:
            letras += 1
    return letras

# main

palabras = [
    "hola",
    "mascota",
    "meritocracia",
    "anarcosindicalista"
]

print("La cantidad de letras en la lista de palabras es " + str(contar(palabras)))
