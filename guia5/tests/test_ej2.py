import pytest
from ej2 import *

# python3 -m pytest -v --cov=ej2

def test_pronunciacion():
    assert 'a' == pronunciacion('a')
    assert 'hache' == pronunciacion('h')
    assert 'jota' == pronunciacion('j')
    assert 'ka' == pronunciacion('k')
    assert 'efe' == pronunciacion('f')
