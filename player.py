import board
import Ship
from random import randint


class Player:
    def __init__(self):
        self.board = board.Board()
        self.ships = [Ship.Ship(decks) for decks in (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)]
        self.all_ships_coordinates = {}
    # x = horizontal, 0; y = vertical, 1

    def ship_placement(self):
        for ship in self.ships:
            while True:
                orientation = randint(0, 1)
                coordinates = []
                if orientation == 0:
                    coordinates = [(randint(0, 10 - ship.decks), randint(0, 9))]
                    for coord in range(1, ship.decks):
                        coordinates.append((coordinates[0][0] + coord, coordinates[0][1]))
                elif orientation == 1:
                    coordinates = [(randint(0, 9), randint(0, 10 - ship.decks))]
                    for coord in range(1, ship.decks):
                        coordinates.append((coordinates[0][0], coordinates[0][1] + coord))
                flag = True
                for n_ship in self.ships:
                    if not flag:
                        break
                    for coordinate in coordinates:
                        for x in range(coordinate[0] - 1, coordinate[0] + 2):
                            for y in range(coordinate[1] - 1, coordinate[1] + 2):
                                if (x, y) in n_ship.coordinates:
                                    flag = False
                                    break
                if flag:
                    ship.coordinates = dict.fromkeys(coordinates, 1)
                    self.all_ships_coordinates.update(ship.coordinates)
                    break


player = Player()


player.ship_placement()

player.board.board_draw(player.all_ships_coordinates)

print(player.all_ships_coordinates)
