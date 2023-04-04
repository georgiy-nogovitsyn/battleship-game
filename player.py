import board
import Ship
from random import randint


class Player:
    def __init__(self):
        self.board = board.Board()
        self.ships = [Ship.Ship(decks) for decks in (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)]
        self.all_pos = []
    # x = horizontal, 0; y = vertical, 1
    def random_ship_placement(self):
        for ship in self.ships:
            while True:
                orientation = randint(0, 1)
                if orientation == 0:
                    coordinates = randint(0, 10 - ship.decks), randint(0, 9)
                elif orientation == 1:
                    coordinates = randint(0, 9), randint(0, 10 - ship.decks)
                pos = [coordinates]
                if orientation == 0:
                    for coord in range(1, ship.decks):
                        pos.append((pos[0][0] + coord, pos[0][1]))
                elif orientation == 1:
                    for coord in range(1, ship.decks):
                        pos.append((pos[0][0], pos[0][1] + coord))
                flag = True
                for n_ship in self.ships:
                    if not flag:
                        break
                    for coords in pos:
                        for x in range(coords[0]-1, coords[0]+2):
                            for y in range(coords[1]-1, coords[1]+2):
                                if (x, y) in n_ship.pos:
                                    flag = False
                                    break

                if flag:
                    ship.pos = pos
                    self.all_pos.extend(pos)
                    break


player = Player()
player.random_ship_placement()

player.board.board_draw(player.all_pos)

print(player.all_pos)
