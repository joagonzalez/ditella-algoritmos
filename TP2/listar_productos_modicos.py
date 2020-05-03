from sys import argv
from producto import Producto

nombre_archivo_stock = argv[1]
nombre_archivo_modicos = argv[2]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def leerCSVdeProductos(nombre_archivo):
	archivo_csv = open(nombre_archivo)
	listado_productos = []
	for linea in archivo_csv:
		listado_productos.append(Producto(linea))
	archivo_csv.close()
	return listado_productos

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

productos_stock = leerCSVdeProductos(nombre_archivo_stock)
productos_modicos = leerCSVdeProductos(nombre_archivo_modicos)

## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def filtrarProductos(stock, modicos):

	productos_filtrados = []

	for p_stock in stock:
		for p_modico in modicos:
			if p_stock == p_modico:
				productos_filtrados.append(p_stock)
	
	return productos_filtrados

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

productos_filtrados = filtrarProductos(productos_stock, productos_modicos)

for producto in productos_filtrados:
	print(producto)
