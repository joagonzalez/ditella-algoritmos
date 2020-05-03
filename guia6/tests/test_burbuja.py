import pytest
from burbuja import booble_order
#from ..burbuja import booble_order

order = [9,5,333,4,5,6,2,1,98,0,34,56,76,11,1,1,3,5,7,67]

def test_burbuja():
    assert [0, 1, 1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 9, 11, 34, 56, 67, 76, 98, 333] == booble_order(order)
