class Producto():
    def __init__(self, data):
        data = data.split(',')
        self._nombre = data[0]
        self._marca = data[1]
        self._pais_de_elaboracion = data[2]
        self._telefono_proveedor = data[3]
        self._direccion_proveedor = data[4]

    def __str__(self):
        return "<{} - {} - {} - {}>".format(self._nombre, self._marca, self._pais_de_elaboracion, self._telefono_proveedor)
    
    def __eq__(self, other):
        return self._nombre == other.nombre() and \
               self._marca == other.marca() and \
               self._pais_de_elaboracion == other.pais_de_elaboracion()
    
    def __lt__(self, other):
        return self._nombre < other.nombre() or \
               self._nombre == other.nombre() and self._marca < other.marca() or \
               self._nombre == other.nombre() and self._marca == other.marca() and self._pais_de_elaboracion < other.pais_de_elaboracion()

    def nombre(self):
        return self._nombre

    def marca(self):
        return self._marca

    def pais_de_elaboracion(self):
        return self._pais_de_elaboracion

    def telefono_proveedor(self):
        return self._telefono_proveedor

    def direccion_proveedor(self):
        return self.direccion_proveedor