import sys
import random

NAMES = ['DJANGO', 'SPECTRE', 'DAEMON', 'HOT ROTT']

class Tateti():

    def __init__(self, jugador):
        # crear juego
        self.juagdor = jugador
        self.ia = NAMES[random.randint(1, len(NAMES)-1)]
        self.moves = self.create_game()
        pass

    def __str__(self):
        pass

    def create_game(self):
        # crear tablero
        pass

    def move(self):
        # carga el movimiento elegido por el jugador
        pass

    def is_end(self):
        # termino el juego?
        pass
