# Definición del tipo Agenda.
class Agenda:

    # Crea una Agenda a partir de los contactos de "contactos.csv".
    def __init__(self):
        self.agenda = []
        archivo = open("contactos.csv")
        self.leer(archivo)        
        archivo.close()

    def leer(self, datos):
        for line in datos:
            contacto = {}
            line = line.split()
            contacto['nombre'] = line[0].replace(',','')
            contacto['mail'] = line[1].replace(',','')
            self.agenda.append(contacto)
        
    # Devuelve el mail del contacto 'nombre'.
    def mail(self, nombre):
        for contacto in self.agenda:
            if contacto['nombre'] == nombre:
                return contacto['mail']       

    # Devuelve el string que representa una agenda, mostrando un
    # contacto por línea. Formato de cada línea: [nombre]: [email]
    # Se tiene que remplazar el cuerpo de la función para que
    # devuelva el string esperado.
    def __str__(self):
        result = ''
        for contacto in self.agenda:
            result += '{}: {}\n'.format(contacto['nombre'], contacto['mail'])
        return result

# Cuerpo principal del programa
agenda = Agenda()
for contacto in ["Alicia", "Juan"]:
    print(contacto + ":", agenda.mail(contacto))

print()
print(agenda)

print(agenda.mail('Martina'))
