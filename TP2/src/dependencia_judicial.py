FILE_ENCODING = 'latin-1'

class DependenciaJudicial():
    """
    Clase que modela una dependencia judicial
    """

    def __init__(self, dependencia):
        """
        Metodo constructor de una dependencia judicial. Se crean todos los atributos
        de una dependencia al instanciarse un objeto de la clase. Se pasa un string
        al cual se aplica un split para separar los datos leidos del archivo csv.
        """
        dependencia = dependencia.split(';')
        self._fuero = dependencia[1]
        self._nombre = dependencia[2]
        self._tipo_de_ente = dependencia[3]
        self._direccion = dependencia[4]
        self._localidad = dependencia[5]
        self._departamento_judicial = dependencia[6]
        self._telefono = dependencia[7]
        self._latitud = dependencia[8].replace(',','.')
        self._longitud = dependencia[9].replace(',','.')

    def __str__(self):
        """
        Metodo para imprimir objetos DependenciaJudicial
        """
        return '{' + '{};{};{};{}'.format(self._fuero, self._nombre, self._direccion, self._localidad) + '}'

    def __eq__(self, other):
        """
        Sobrecarga de operador == con metodo __eq__ en base a:
        departamento_judicial, fuero, nombre de la dependencia
        """
        return self._departamento_judicial == other.departamento_judicial() and \
               self._fuero == other.fuero() and \
               self._nombre == other.nombre()

    def __lt__(self, other):
        """
        Sobrecarga de operador < con metodo __lt__ en base a:
        departamentos judiciales, fueros, nombres
        """
        return self._departamento_judicial < other.departamento_judicial() or \
               self._departamento_judicial == other.departamento_judicial() and self._fuero < other.fuero() or \
               self._departamento_judicial == other.departamento_judicial() and self._fuero == other.fuero() and self._nombre < other.nombre()

    def fuero(self):
        """
        Retornamos atributo fuero de la dependencia
        """
        return self._fuero

    def nombre(self):
        """
        Retornamos atributo nombre de la dependencia
        """
        return self._nombre

    def tipo_de_ente(self):
        """
        Retornamos atributo tipo_de_ente de la dependencia
        """
        return self._tipo_de_ente

    def direccion(self):
        """
        Retornamos atributo direccion de la dependencia
        """
        return self._direccion

    def localidad(self):
        """
        Retornamos atributo localidad de la dependencia
        """
        return self._localidad

    def departamento_judicial(self):
        """
        Retornamos atributo departamento_judicial de la dependencia
        """
        return self._departamento_judicial

    def telefono(self):
        """
        Retornamos atributo telefono de la dependencia
        """
        return self._telefono

    def distancia(self, lat, long):
        """
        Retornamos distancia euclidea entre dependencia juficial
        y el punto que se pasa como parametro del metodo
        """
        return ((float(self._latitud) - lat)**2 + (float(self._longitud) - long)**2)**0.5

def abrir_archivo(filename):                            # O(2*len(dependencias))
    """
    funcion que nos permite abrir archivo de dependencias
    tratando excepciones. Da como salida una lista donde 
    cada elemento tiene la informacion de una dependencia
    """
    dependencias = []                                   # O(1)
    lineas = []                                         # O(1)

    try:
        f = open(filename, encoding=FILE_ENCODING)      # O(1)
        for linea in f:                                 # O(len(dependencias))
            lineas.append(linea)                        # O(1)
        f.close()                                       # O(1)
        
        lineas = lineas[1:] # se limpian headers del csv    # O(1)
        
        for dependencia in lineas:                      # O(len(dependencias))
            dependencias.append(DependenciaJudicial(dependencia))   # O(1)

        return dependencias                             # O(1)
    except FileNotFoundError as e:
        print('El archivo no existe. \n' + str(e))      # O(1)
        return None                                     # O(1)
    except Exception as e:
        print('Error al abrir el archivo. \n' + str(e)) # O(1)
        return None                                     # O(1)

if __name__ == '__main__':
    dependencias = abrir_archivo('../data/mapa-judicial.csv')
    # print(dependencias)
    print(dependencias[0])
    print(dependencias[0].fuero())
    print(dependencias[0].nombre())
    print(dependencias[0].tipo_de_ente())
    print(dependencias[0].direccion())
    print(dependencias[0].localidad())
    print(dependencias[0].departamento_judicial())
    print(dependencias[0].telefono())
    print(dependencias[0].distancia(-36.77571, -59.0886))

    print(dependencias[0] == dependencias[0])
    print(dependencias[0] == dependencias[1])
    print(dependencias[0] < dependencias[1])
    print(dependencias[1] < dependencias[0])
