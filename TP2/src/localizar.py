import sys
from dependencia_judicial import DependenciaJudicial, abrir_archivo

FOLDER = '../data/'

def localizar_dj(dependencias, latitud, longitud):
    """
    Funcion que permite localizar la dependencia judicial mas cercana a 
    los parametros de longitud y latitud ingresados como parametro.
    """
    resultado = dependencias[0]

    for dependencia in dependencias:
        if dependencia._latitud != '' and dependencia._longitud != '':
            if dependencia.distancia(latitud, longitud) < resultado.distancia(latitud, longitud):
                resultado = dependencia

    return resultado

# $ python3 localizar.py mapa-judicial.csv -36.77571 -59.0886
if __name__ == '__main__':
    try:
        FILENAME = FOLDER + sys.argv[1]
        LATITUD = float(sys.argv[2])
        LONGITUD = float(sys.argv[3])
    except Exception as e:
        print('Los parametros <FILENAME> <LATITUD> <LONGITUD> no fueron ingresados correctamente. \n' + str(e))


    dependencias = abrir_archivo(FILENAME)

    # for dependencia in dependencias:
    #     print(dependencia)
    #     print(dependencia.distancia(LATITUD, LONGITUD))

    print(localizar_dj(dependencias, LATITUD, LONGITUD))
