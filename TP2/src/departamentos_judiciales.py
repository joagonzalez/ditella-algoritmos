import sys
from dependencia_judicial import DependenciaJudicial, abrir_archivo

FOLDER = '../data/'

def bubble_sort(lista):                     # O(len(lista)^2)
    """
    Implementacion de algoritmo Bubble Sort O(n^2)
    Se pueden ordenar las listas de dependencias por departamente 
    haciendo uso de la sobrecarga del operador < para los objetos
    de la clase DependenciaJudicial()
    """
    i = 0                                   # O(1)
    j = 0                                   # O(1)

    for i in range(len(lista)-1):           # O(len(lista))
        for j in range(len(lista)-1):       # O(len(lista))
            aux = lista[j]                  # O(1)

            if lista[j+1] < lista[j]:       # O(1)
                lista[j] = lista[j+1]       # O(1)
                lista[j+1] = aux            # O(1)

    return lista                            # O(1)

def formatear(dependencias):                                                # O(len(departamentos)*len(dependencias))
    """
    Funcion que recibe una lista de objetos DependenciaJudicial y genera 
    un diccionario con key = departamento y value = lista de dependencias
    de ese departamento. La lista se ordenara posteriormente por key
    """
    # guardamos departamentos en conjunto, ya que no queremos elementos repetidos
    departamentos = set()                                                   # O(1)
    resultado = {}                                                          # O(1)

    for dependencia in dependencias:                                        # O(len(dependencias))
        departamentos.add(dependencia.departamento_judicial())              # O(1)

    for departamento in departamentos:                                      # O(len(departamentos)*len(dependencias))
        # inicializamos lista por cada iteracion de departamento
        dependencias_en_departamento = []                                   # O(1)
        for dependencia in dependencias:                                    # O(len(dependencias))
            if departamento == dependencia.departamento_judicial():         # O(1)
                 dependencias_en_departamento.append(dependencia)           # O(1)
        # se guardan todas las dependencias de un departamento en un diccionario key=deparamento
        resultado[departamento] = dependencias_en_departamento              # O(1)

    return resultado                                                        # O(1)

def guardar_dependencias(lista_departamentos, dependencias_por_departamento, filename): # O(len(departamentos)*len(dependencias))
    """
    Funcion que recibe como parametro una lista de dependencias correctamente
    formateadas y el nombre del archivo en el que se guardaran los resultados 
    """
    try:
        f = open(filename, 'w')                                             # O(1)
    except Exception as e:
        print('Error al crear el archivo de destino' + str(e))              # O(1)

    for departamento in lista_departamentos:                                # O(len(departamentos)*len(dependencias))
        f.write(departamento + ': ')                                        # O(1)
        for dependencia in dependencias_por_departamento[departamento]:     # O(len(dependencias))
            f.write(str(dependencia))                                       # O(1)
        f.write('\n')                                                       # O(1)
    f.close()                                                               # O(1)

# $ python3 departamentos_judiciales.py mapa-judicial.csv departamentos.txt
if __name__ == '__main__':
    try:                                                                    # string concat O(M+N)    
        SRC_FILENAME = FOLDER + sys.argv[1]                                 # O(len(FOLDER) + len(len(sys.argv[1])))
        DST_FILENAME = FOLDER + sys.argv[2]                                 # O(len(FOLDER) + len(len(sys.argv[2])))
    except Exception as e:
        print('Los parametros <SRC FILENAME> <DST FILENAME> no fueron ingresados correctamente. \n' + str(e))    # O(1)

    dependencias = abrir_archivo(SRC_FILENAME)                              # O(2*len(dependencias))
    dependencias_formateadas = formatear(dependencias)                      # O(len(dependencias)*len(departamentos))

    # Ordenamos departamentos (llaves del diccionario que devuelve funcion formatear)
    departamentos_ordenados = sorted(dependencias_formateadas.keys())       # O(len(departamentos)*log(len(departamentos)))

    # Ordenamos las dependencias de todos los departamentos 
    for departamento, dependencias in dependencias_formateadas.items():     # O(len(departamentos)*(len(dependencias)*log(len(dependencias)))
        dependencias_formateadas[departamento] = sorted(dependencias_formateadas[departamento])   # O(len(dependencias)*log(len(dependencias)))
        #bubble_sort(dependencias_formateadas[departamento])                # O(len(dependencias)^2) - Si usaramos implementacion propia de bubble_sort

    # Guardamos los datos en el formato y orden requerido 
    guardar_dependencias(departamentos_ordenados, dependencias_formateadas, DST_FILENAME)   # O(len(departamentos)*len(dependencias))
