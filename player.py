import board
import ship_class
from random import randint


class Player:
    def __init__(self):
        self.board = board.Board()
        self.ships = [ship_class.Ship(decks) for decks in (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)]
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
                for check_ship in self.ships:
                    if not flag:
                        break
                    for coordinate in coordinates:
                        for y in range(coordinate[0] - 1, coordinate[0] + 2):
                            for x in range(coordinate[1] - 1, coordinate[1] + 2):
                                if (y, x) in check_ship.coordinates:
                                    flag = False
                                    break
                if flag:
                    ship.coordinates = dict.fromkeys(coordinates, 1)
                    self.all_ships_coordinates.update(ship.coordinates)
                    # for coordinate in ship.coordinates:
                    #     self.board.field.pop(coordinate)
                    #     self.board.battlefield.pop(coordinate)  # opponent battlefield
                    break

    def attack(self, opponent_ships, opponent_field):
        def user_input():
            xz = input('Input: ')
            choice = []
            for x in xz:
                choice.append(int(x))
            return tuple(choice)

        flag = False
        while True:
            choice = user_input()
            for ship in opponent_ships:
                if choice in ship.coordinates:
                    if ship.coordinates[choice] == 1:
                        ship.coordinates[choice] = 0
                        print(f'get the ship {choice}')
                        flag = True
                        break
                    elif ship.coordinates[choice] == 0:
                        choice = user_input()
            if flag:
                break
            else:
                if self.board.battlefield[choice] == 1:
                    print(f'missed {choice}')
                    self.board.battlefield[choice] = 0
                    opponent_field[choice] = 0
                    break

# [-1][-1]     [-1][+1]
#         0 0 0
#         0 x 0
#         0 0 0
# [+1][-1]     [+1][+1]
