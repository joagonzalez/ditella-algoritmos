# ej3
import sys

print(str(sys.float_info))

""" No se utiliza == con floats por que 
0.66666 y 0.66667 podrian ser igual para mi
aplicacion pero si hacemos float1 == float2 daria
False. Para esto cambiamos el approach de comparacion
y pasamos a usar abs(float1 - float2) < epsilon dado 
epsilon una resolucion deseada"""