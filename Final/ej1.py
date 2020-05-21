import sys

COFRES = [[0,1,2,3], [5,6,10,7,8], [2,4,6,8], [9,1,2,4]]

def altbool(n):
    x = [True, False]
    l = [ x[i%2] for i in range(int(n)) ]
    return l

def busco_carta(c):                 # O(len(COFRES) * len(mazo)) en el peor de los casos
    i = 0
    for cofre in COFRES:            # O(len(COFRES))
        i += 1                      # O(1)
        _ok = False                 # O(1)
        for carta in cofre:         # O(len(mazo))
            if carta == c:          # O(1)
                print('encontramos la carta en el mazo ' + str(i)) # O(1)
                _ok = True          # O(1)
        if _ok:                     # O(1)
            break                   # O(1)
                
    return i                        # O(1)

if __name__ == '__main__':
    param = sys.argv[1]
    carta = sys.argv[2]
    print(altbool(param))                
    print(busco_carta(int(carta)))