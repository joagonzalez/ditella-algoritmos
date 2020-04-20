import pytest
from ej6 import Queue

@pytest.fixture
def queue():
    # fixture para inyectar objectos queue en tests
    return Queue()

def test_constructor(queue):
    assert True == queue.empty() 
    assert len(queue) == 0

def test_enqueue(queue):
    queue.enqueue('joaquin')
    assert 'joaquin' == queue.first()
    queue.enqueue(1)
    assert 'joaquin' == queue.first()

def test_dequeue(queue):
    queue.enqueue('joaquin')
    queue.enqueue(1)
    assert False == queue.empty()
    queue.dequeue()
    assert 1 == queue.first()
    queue.dequeue()
    assert True == queue.empty()
