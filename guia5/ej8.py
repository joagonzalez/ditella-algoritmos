import sys
import random

NAMES = ['DJANGO', 'SPECTRE', 'DAEMON', 'HOT ROTT']

class Tateti():

    def __init__(self, player):
        # crear juego
        self.player = player
        self.player_symbol = ''
        self.ia = NAMES[random.randint(1, len(NAMES)-1)]
        self.board = [' '] * 10
        self.playing = False

    def __str__(self):
        if self.playing:
            msg = '{} esta jugando contra {}'.format(self.player, self.ia)
        else:
            msg = '{} jugo contra {}'.format(self.player, self.ia)
        
        return msg

    def choose_symbol(self):
        result = None
        symbols = ['X', 'O']

        while symbol not in symbols:
            result = input('Ingrese su equipo [X/O]: ')

        self.player_symbol = result

    def player_move(self):
        # carga el movimiento elegido por el jugador
        result = None
        
        while result not in range(1,9):
            result = input('Ingrese su proximo movimiento (1-9): ')
        
        self.board[result] = self.player_symbol

    def is_end(self):
        result = None
        if ' ' not in self.tablero:
            result = True
        else:
            result = False

    def play_again(self):
        result = input('Desea volver a jugar? (s/n): ').lower()

        while 's' not in result and 'n' not in result:
            result = input('Desea volver a jugar? (s/n): ').lower()

        return result

    def     (self, board):
        """ 
        Esta función dibuja el tablero recibido como argumento.
        "tablero" es una lista de 10 cadenas representando la pizarra (ignora índice 0)
        """
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

def __name__ == '__main__':
    pass