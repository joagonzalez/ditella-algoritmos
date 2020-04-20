import pytest
from ej4 import Stack
from ej7 import Atencion

@pytest.fixture
def turnero():
    return Atencion()

def test_llega(turnero):
    turnero.llega('joaquin', 'vip')
    assert 'joaquin' == turnero.proximo()
    turnero.llega('mora', 'vip')
    assert 'joaquin' == turnero.proximo()

def test_vacia(turnero):
    assert True == turnero.vacia()
    turnero.llega('joaquin', 'vip')
    assert False == turnero.vacia()

def test_atender(turnero):
    turnero.llega('joaquin', 'vip')
    turnero.llega('mora', 'comun')
    
    assert 'joaquin' == turnero.proximo()
    turnero.atender()
    assert 'mora' == turnero.proximo()
    turnero.atender()
    assert None == turnero.proximo()
    
    

