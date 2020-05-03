import sys
from dependencia_judicial import DependenciaJudicial, abrir_archivo






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
