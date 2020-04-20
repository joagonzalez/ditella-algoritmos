import pytest
from ej4 import Stack
from ej5 import balanced_string

@pytest.fixture
def stack():
    return Stack()

def test_balanced_string():
    msg_1 = '{a(b)x[()]}'
    msg_2 = '[()()]'
    msg_3 = '}'
    msg_4 = 'a(b))'
    msg_5 = '[[})'
    msg_6 = 'hola'
    
    assert True == balanced_string(msg_1)
    assert True == balanced_string(msg_2)
    assert False == balanced_string(msg_3)
    assert False == balanced_string(msg_4)
    assert False == balanced_string(msg_5)
    assert True == balanced_string(msg_6)
