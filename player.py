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
                    coordinates = randint(0, 9 - ship.decks + 1), randint(0, 9 - ship.decks + 1)
                elif orientation == 1:
                    coordinates = randint(0, 9 - ship.decks + 1), randint(0, 9 - ship.decks + 1)
                pos = [orientation, ship.decks, coordinates]
                if pos[0] == 1:
                    for coord in range(1, pos[1]):
                        pos.append((pos[2][0] + coord, pos[2][1]))
                elif pos[0] == 0:
                    for coord in range(1, pos[1]):
                        pos.append((pos[2][0], pos[2][1] + coord))
                flag = True
                for n_ship in self.ships:
                    if not flag:
                        break
                    for coords in pos[2:]:  # need to refactor
                        if coords in n_ship.pos:
                            flag = False
                            break
                        if (coords[0] + 1, coords[1] + 1) in n_ship.pos:
                            flag = False
                            break
                        if (coords[0] - 1, coords[1] - 1) in n_ship.pos:
                            flag = False
                            break
                        if (coords[0] - 1, coords[1]) in n_ship.pos:
                            flag = False
                            break
                        if (coords[0], coords[1] - 1) in n_ship.pos:
                            flag = False
                            break
                        if (coords[0] + 1, coords[1]) in n_ship.pos:
                            flag = False
                            break
                        if (coords[0], coords[1] + 1) in n_ship.pos:
                            flag = False
                            break
                        if (coords[0] - 1, coords[1] + 1) in n_ship.pos:
                            flag = False
                            break
                        if (coords[0] + 1, coords[1] - 1) in n_ship.pos:
                            flag = False
                            break
                        if (coords[0] + 1, coords[1] - 1) in n_ship.pos:
                            flag = False
                            break
                        if (coords[0] - 1, coords[1] + 1) in n_ship.pos:
                            flag = False
                            break

                if flag:
                    ship.pos = pos
                    self.all_pos.extend(pos[2:])
                    break


player = Player()
player.random_ship_placement()

player.board.board_draw(player.all_pos)

print(player.all_pos)
