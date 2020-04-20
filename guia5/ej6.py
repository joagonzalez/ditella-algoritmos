import sys

class Queue():

    def __init__(self):
        self.queue = []

    def __str__(self):
        if self.empty():
            return 'La cola esta vacia'
        else:
            return 'El ultimo elemento de la pila es {} sobre {} elementos'.format(self.queue[len(self.queue)-1], len(self.queue))

    def __len__(self):
        return len(self.queue)
        
    def empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
    # en vez de quitar el ultimo elemento (stack) quito el primero
        if not self.empty():
            self.queue.remove(self.queue[0])

    def first(self):
    # en vez de quitar el ultimo elemento (stack) quito el primero
        if not self.empty():
            return self.queue[0]
        else:
            return None

if __name__ == '__main__':
    cola = Queue()

    print(cola.empty())
    print(cola.first())
    cola.enqueue('joaquin')
    print(len(cola))
    cola.enqueue('mora')
    print(len(cola))
    print(cola.first())
    cola.dequeue()
    print(cola.first())
    cola.dequeue()
    print(cola.first())
    cola.dequeue()
    print(cola.first())
