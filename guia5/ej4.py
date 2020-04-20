import sys

class Stack():
    def __init__(self):
        self.stack = []
    
    def __str__(self):
        if self.empty():
            return 'La pila esta vacia'
        else:
            return 'El ultimo elemento de la pila es {} sobre {} elementos'.format(self.stack[len(self.stack)-1], len(self.stack))

    def __len__(self):
        return len(self.stack)
        
    def push(self, element):
        self.stack.append(element)
    
    def empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    
    def top(self):
        if self.empty():
            return None
        else:
            return self.stack[len(self.stack)-1]
    
    def pop(self):
        if not self.empty():
            self.stack.remove(self.stack[len(self.stack)-1])

if __name__ == '__main__':
    # main program
    stack = Stack()
    print(stack.empty())
    print(len(stack))
    stack.push(1)
    print(stack)
    stack.push(321)
    stack.push('hola')
    print(stack.top())
    print(stack)
    stack.pop()
    print(stack.empty())
    print(stack)
    print(len(stack))