import sys
import logging

def contar_palabras(linea):
    linea = linea.split()
    return len(linea)

def analizar_texto(fh):
    texto = fh.read()
    result = []
    texto_lista = texto.split('\n')

    for linea in texto_lista:
        result.append(contar_palabras(linea))

    return [texto, result]

def abrir_archivo(filename):
    try:
        f = open(filename, 'r')
        logging.info('archivo abierto ok')
    except FileNotFoundError:
        logging.error('error al abrir archivo ' + filename)
    
    return f

def guardar_archivo(texto):
    try:
        f = open('out.txt', 'w')
        logging.info('archivo abierto ok')
    except FileNotFoundError:
        logging.error('error al abrir archivo ' + filename)
    
    f.write(str(texto))
    f.close()

def mostrar_resultados(lista):
    i = 0
    for element in lista:
        print('la linea ' + str(i) + ' tiene ' + str(element) + ' palabras')
        i += 1

# main
# print('La cantidad de palabras del texto es: ', contar_palabras(sys.argv[1:]))

f = abrir_archivo(sys.argv[1])
texto, result = analizar_texto(f)

print('texto: ', texto)
mostrar_resultados(result)
guardar_archivo(result)

