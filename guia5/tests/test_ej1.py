import pytest
from ej1 import *

# python3 -m pytest -v --cov=ej1

frases = [
        "hola mundo",
        "oh mundo cruel, en el que vive gente asi",
        "cruel es el mundo en donde la gente que vive es asi"
        ]

def test_intersection():
    a = set([1,2,3])
    b = set([3, 4])

    c = set([1,2,3,5,6,7,8])
    d = set([2,3,8,12,34,56])

    assert set([3]) == intersection(a,b)
    assert set([2,3,8]) == intersection(c,d)

def test_union():
    a = set([1,2,3])
    b = set([3, 4])

    c = set([1,2,3,5,6,7,8])
    d = set([2,3,8,12,34,56])

    assert set([1,2,3,4]) == union(a,b)
    assert set([1,2,3,5,6,7,8,12,34,56]) == union(c,d)

def test_k_shingles():
    k = 5

    assert set([' mund', 'ola m', 'a mun', 'mundo', 'la mu', 'hola ']) == k_shingles(frases[0], k)
    assert set(['l que', 've ge', 'el qu', 'ndo c', 'h mun', ' gent', 'n el ', ' mund', 'uel, ', 'mundo', 'oh mu', 'l, en', 'vive ', 'o cru', 'e viv', 'nte a', ', en ', 'cruel', 'en el', 'te as', 'ue vi', ' en e', ' que ', ' vive', 'que v', 'gente', ' crue', 'ruel,', 'undo ', 'ive g', 'e gen', 'do cr', ' el q', 'e asi', 'ente ', 'el, e']) == k_shingles(frases[1], k)

def test_jaccard():
    a = set([1,2,3])
    b = set([3, 4])
    c = k_shingles(frases[1], 5)
    d = k_shingles(frases[2], 5)

    assert 0.25 == jaccard(a,b)
    assert 0.18571428571428572 == jaccard(c,d)