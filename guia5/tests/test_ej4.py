import pytest
from ej4 import Stack

@pytest.fixture
def stack():
    return Stack()
    # fixture para inyectar objectos stack en tests

def test_constructor():
    l1 = Stack()
    assert True == l1.empty() 
    assert len(l1) == 0

def test_push(stack):
    stack.push(1)
    assert 1 == stack.top()
    stack.push('hola')
    assert 'hola' == stack.top()

def test_pop(stack):
    stack.push(1)
    stack.pop()
    assert True == stack.empty()
