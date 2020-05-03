import sys
from dependencia_judicial import DependenciaJudicial, abrir_archivo

FOLDER = '../data/'

def localizar_dj(dependencias, latitud, longitud):                                     # O(len(dependencias))
    """
    Funcion que permite localizar la dependencia judicial mas cercana a 
    los parametros de longitud y latitud ingresados como parametro.
    """
    resultado = dependencias[0]                                                        # O(1)

    for dependencia in dependencias:                                                   # O(len(dependencias))
        if dependencia._latitud != '' and dependencia._longitud != '':                 # O(1)
            if dependencia.distancia(latitud, longitud) < resultado.distancia(latitud, longitud): # O(1)
                resultado = dependencia                                                # O(1)

    return resultado                                                                   # O(1)

# $ python3 localizar.py mapa-judicial.csv -36.77571 -59.0886
if __name__ == '__main__':
    try:
        FILENAME = FOLDER + sys.argv[1]                                                # O(1)
        LATITUD = float(sys.argv[2])                                                   # O(1)
        LONGITUD = float(sys.argv[3])                                                  # O(1)
    except Exception as e:
        print('Los parametros <FILENAME> <LATITUD> <LONGITUD> no fueron ingresados correctamente. \n' + str(e)) # O(1)


    dependencias = abrir_archivo(FILENAME)                                             # O(2*len(dependencias))

    # for dependencia in dependencias:
    #     print(dependencia)
    #     print(dependencia.distancia(LATITUD, LONGITUD))

    print(localizar_dj(dependencias, LATITUD, LONGITUD))                               # O(len(dependencias))
