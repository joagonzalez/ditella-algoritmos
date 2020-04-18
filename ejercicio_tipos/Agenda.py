# Definición del tipo Agenda.
class Agenda:

    # Crea una Agenda a partir de los contactos de "contactos.csv".
    def __init__(self):
        archivo = open("contactos.csv")
        pass            # [reemplazar]
        archivo.close()

    # Devuelve el mail del contacto 'nombre'.
    def mail(self, nombre):
        return ""       # [reemplazar]

    # Devuelve el string que representa una agenda, mostrando un
    # contacto por línea. Formato de cada línea: [nombre]: [email]
    # Se tiene que remplazar el cuerpo de la función para que
    # devuelva el string esperado.
    def __str__(self):
        return ""       # [reemplazar]

# Cuerpo principal del programa
agenda = Agenda()
for contacto in ["Alicia", "Juan"]:
    print(contacto + ":", agenda.mail(contacto))

print()
print(agenda)
