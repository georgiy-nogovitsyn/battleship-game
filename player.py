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
                    break

    def attack(self, opponent_ships, opponent_field):
        flag = False, False
        while True:
            if flag == (True, True):
                break
            else:
                flag = False, False
            while True:
                player_input = input('Enter the x, y coordinates from 00 to 99, e.g. 37: ')
                if player_input.isdigit() and len(player_input) == 2:
                    # print(player_input)
                    choice = int(player_input[0]), int(player_input[1])
                    print(choice)
                    break
                else:
                    print('Input is not valid.')
            for ship in opponent_ships:
                if choice in ship.coordinates:
                    if ship.coordinates[choice] == 1:
                        print('Ship is on fire!')
                        ship.coordinates[choice] = 0
                        flag = True, True
                        break
                    elif ship.coordinates[choice] == 0:
                        print('You already hit that cell')
                        flag = True, False
                        break
            if flag == (True, True):
                break
            elif flag == (True, False):
                continue
            else:
                for i, row in enumerate(self.board.battlefield):
                    if choice in row:
                        if row[choice] == 1:
                            print('Missed.')
                            row[choice] = 0
                            opponent_field[i][choice] = 0
                            flag = True, True
                            break
                        elif row[choice] == 0:
                            print('You already hit that cell')
                            break


# [-1][-1]     [-1][+1]
#         0 0 0
#         0 x 0
#         0 0 0
# [+1][-1]     [+1][+1]
