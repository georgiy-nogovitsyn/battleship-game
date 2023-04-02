import board, ship
from random import randint, choice


class Player:
    def __init__(self):
        self.board = board.Board()
        self.ships = [ship.Ship(decks) for decks in [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]]

    #x = horiz 0, y = vertical 1
    def random_ship_placement(self):
        board_imitate = [[0 for x in range(10)] for x in range(10)]
        for ship in self.ships:
            while True:
                cell = randint(0, 10), randint(0,10), randint(0,1)


    def coords_validation(self, cell):
