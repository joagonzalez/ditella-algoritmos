import sys

def base_2(n):
    base = 2
    result = []
    aux = n
    
    if n > base-1:
        while aux != 0:
            if aux % base == 0:
                result.append(0)
            else:
                result.append(1)
            aux = int(aux / base)
        result.reverse()
    else:
        result.append(aux)
    
    return result    


def base_16(n):
    base = 16
    map = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    aux = n
    result = []
    if n > base-1:
        while aux != 0:
            if aux % base == 0:
                result.append(map[0])
            else:
                result.append(map[int(aux%base)])
            aux = int(aux / base)
    else:
        result.append(map[aux])
        
    result.reverse()
    return result

# main
# $ python3 ej7.py 26
# numero base 2: [1, 1, 0, 1, 0]
# numero base 16: ['1', 'A']

n = None
try:
    n = int(sys.argv[1])
except:
    print('ingresar parametros correctos!')

if n is not None:
    print('numero base 2: ' + str(base_2(n)))
    print('numero base 16: ' + str(base_16(n)))