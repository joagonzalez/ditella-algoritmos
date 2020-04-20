import sys
from ej6 import Queue


# hay que cambiar Stack por Queue sino el primero en llegar sera el ultimo en ser atendido
class Atencion():

    def __init__(self):
        self.vip = Queue()
        self.comun = Queue()

    def __str__(self):
        return 'Cliente en cola vip: {} y en cola comun: {}'.format(len(self.vip), len(self.comun))

    def llega(self, c, p):
        """
        c = cliente (nombre)
        p = prioridad (vip, comun)
        """
        if p.lower() == 'vip':
            self.vip.enqueue(c)
        elif p.lower() == 'comun':
            self.comun.enqueue(c)
    
    def vacia(self):
        if self.vip.empty() and self.comun.empty():
            return True
        else:
            return False

    def atender(self):
        if not self.vacia():
            if self.vip.empty():
                self.comun.dequeue()
            else:
                self.vip.dequeue()

    def proximo(self):
        if not self.vacia():
            if self.vip.empty():
                return self.comun.first()
            else:
                return self.vip.first()
        else:
            return None

if __name__ == '__main__':
    turnero = Atencion()

    turnero.llega('joaquin', 'vip')
    turnero.llega('mora', 'vip')
    turnero.llega('pedro', 'comun')
    turnero.llega('gaston', 'Comun')
    turnero.llega('pichiruli', 'comun')
    
    print(turnero)
    turnero.atender()
    print(turnero)
    turnero.atender()
    print(turnero)
    turnero.atender()
    print(turnero)
    turnero.atender()
    print(turnero)
    turnero.atender()
    print(turnero)
    turnero.atender()
    print(turnero)