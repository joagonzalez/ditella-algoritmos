import sys

def invertir_string(palabra):
    palabra_inv = ""
    size = int(len(palabra))

    for i in range(size):
        palabra_inv += palabra[size-i-1]

    return palabra_inv


text = "!ecneics retupmoc nioj"
print(invertir_string(text))