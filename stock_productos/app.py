import sys
from producto import Producto

# Funciones 
def openFile(filename):
    f = open(filename)                                                  # O(1)
    productos = []                                                      # O(1)
    for line in f:                                                      # O(K)         
        productos.append(Producto(line))                                # O(1)
    f.close()                                                           # O(1)

    return productos                                                    # O(1)
                                                                        # TOTAL = O(K)
def printProducts(list):
    for product in list:                                                
        print(product)

# __main__

if __name__ == '__main__':
    file1 = sys.argv[1]                                                 # O(1)
    file2 = sys.argv[2]                                                 # O(1)

    stock = openFile(file1)                                             # O(N) - N elementos
    precios_modicos = openFile(file2)                                   # O(M) - M elementos
    productos_filtrados = []                                            # O(1)

    print('Productos stock: ' + str(len(stock)))                        # O(1)
    print('Productos modicos: ' + str(len(precios_modicos)))            # O(1)

    for prod_stock in stock:                                            # O(N)    
        for prod_modico in precios_modicos:                             # O(M)
            if prod_stock == prod_modico:                               # O(1)
                productos_filtrados.append(prod_stock)                  # O(1)
                                                                        # TOTAL = O(M*N) pues M*N mayor a N y a M

    productos_filtrados.sort()                                          # O(N*log(N))
    printProducts(productos_filtrados)                                  # O(1)


# TOTAL = O(N*M) + O(N*log(N))