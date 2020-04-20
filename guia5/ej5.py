import sys
from ej4 import Stack


def paired(letter):
    if letter == '(':
        return ')'
    elif letter == '[':
        return ']'
    elif letter == '{':
        return '}'

def balanced_string(phrase):
    """
    Cada nuevo {} o [] o () de apertura sera incluido en la pila con el metodo push
    Si se encuentra el elemento de cierre se removera de la pila con el metodo pop
    Aqui se evalua que el top de stack coincidad con la letra a remover, sino sera desbalanceado
    Si, al finalizar la iteracion sobre la frase, la pila queda vacia (empty == True)
    entonces la frase estara balanceada
    """
    stack = Stack()

    for letter in phrase:
        if letter == '(' or letter == '[' or letter == '{':
            stack.push(letter)
            print('inserto ' + letter)
        elif letter == ')' or letter == ']' or letter == '}':
            if stack.empty() or paired(stack.top()) != letter:
                print(stack.top())
                print(letter)
                print(paired(letter))
                print('no cumple')
                return False # no balanceado
            else:
                stack.pop()
                print('remuevo ' + letter)
    
    if stack.empty():
        return True
    else:
        return False


if __name__ == '__main__':
    
    msg = ""

    while True:
        msg = input('Ingrese un string para analizar o [s/salir]: ')
        msg = msg.lower()

        if msg == 's' or msg == 'salir':
            break

        if balanced_string(msg):
            print('el string que introdujo esta balanceado')
        else:
            print('el string que introdujo no esta balanceado')

        