import sys
from functools import total_ordering

@total_ordering
class Fecha():
    
    def __init__(self, d, m, a):
        # se asume fecha ingresada valida
        # se asume todos los meses 31 dias
        self.dia = d
        self.mes = m
        self.ano = a

    def __str__(self):
        return '{}/{}/{}'.format(self.dia, self.mes, self.ano) 

    def __cmp__(self, other):
        if (self.ano < other.ano) or (self.ano == other.ano and self.mes < other.mes) or (self.ano == other.ano and self.mes == other.mes and self.dia < other.dia):
            return -1
        elif (self.ano == other.ano and self.mes == other.mes and self.dia == other.dia):
            return 0
        else:
            return 1    

    def __le__(self, other):
        if (self.ano < other.ano) or (self.ano == other.ano and self.mes < other.mes) or (self.ano == other.ano and self.mes == other.mes and self.dia < other.dia):
            return True
        else:
            return False

    def siguiente(self):
        dia = self.dia
        mes = self.mes
        ano = self.ano

        if int(self.dia) < 31:
            dia = dia + 1
        else:
            dia = 1
            
        if int(self.mes) < 12 and int(self.dia) == 31:
            mes = mes + 1

        if int(self.mes) == 12 and self.dia == 31:
            ano = ano + 1
            mes = 1
        else: 
            ano = ano

        # Se retorna un objeto de tipo fecha con la siguiente fecha
        nueva_fecha = Fecha(dia, mes, ano)

        return nueva_fecha       

def cant_dias(fecha1, fecha2):
    cantidad = 0
    while fecha1 < fecha2:
        # print(fecha1)
        cantidad = cantidad + 1
        fecha1 = fecha1.siguiente()
    return cantidad
 
if __name__ == '__main__':
        
    fecha1 = Fecha(10,1,2001)
    fecha2 = Fecha(31,12,1999)
    print(fecha1.dia, fecha1.mes, fecha1.ano)
    print(fecha1.siguiente())
    print(fecha2.dia, fecha2.mes, fecha2.ano)
    print(fecha2.siguiente())
    print(fecha2<fecha1)

    print('Cantidad de dias entre el {} y el {} es: {}'.format(fecha2, fecha1, cant_dias(fecha2, fecha1)))