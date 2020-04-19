import pytest
from ej3 import *

def test_siguiente():
    fecha1 = Fecha(10,1,2001)
    fecha2 = Fecha(31,12,1999)
    fecha3 = Fecha(1,1,2000)
    fecha4 = Fecha(11,1,2001)
    assert fecha4.dia == fecha1.siguiente().dia
    assert fecha4.mes == fecha1.siguiente().mes
    assert fecha4.ano == fecha1.siguiente().ano

    assert fecha3.dia == fecha2.siguiente().dia
    assert fecha3.mes == fecha2.siguiente().mes
    assert fecha3.ano == fecha2.siguiente().ano

def test_cant_dias():
    fecha1 = Fecha(10,1,2001)
    fecha2 = Fecha(31,12,1999)

    assert 382 == cant_dias(fecha2, fecha1)