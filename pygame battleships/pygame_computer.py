
import pygame_board
import ship_class
from random import randint, choice as ch


class Comp:
    def __init__(self):
        self.board = pygame_board.Board()
        self.ships = [ship_class.Ship(decks) for decks in (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)]
        self.ship_placement()

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
                    break

    def attack(self, opponent_ships, opponent_field):
        flag = False, False
        ship_hit = False
        while True:
            if flag == (True, True):
                break
            elif flag != (False, False):
                flag = False, False
            local_flag = True
            for ship in opponent_ships:
                if local_flag is False:
                    break
                if 0 in ship.coordinates.values() and ship.status is True:
                    coordinates_for_choice = []
                    for coordinate in ship.coordinates:
                        if local_flag is False:
                            break
                        if ship.coordinates[coordinate] == 0:
                            for x in range(coordinate[0] - 1, coordinate[0] + 2):
                                if local_flag is False:
                                    break
                                for y in range(coordinate[1] - 1, coordinate[1] + 2):
                                    if local_flag is False:
                                        break
                                    if 9 >= x >= 0 and 9 >= y >= 0 and (x, y) != coordinate:
                                        if ship.coordinates.get((x, y)) != 0 and self.board.battlefield[x, y] != 0:
                                            coordinates_for_choice.append((x, y))
                    else:
                        choice = ch(coordinates_for_choice)
                        local_flag = False
                        break

            if local_flag is True:
                choice = randint(0, 9), randint(0, 9)
            for ship in opponent_ships:
                if choice in ship.coordinates:
                    if ship.coordinates[choice] == 1:
                        ship.coordinates[choice] = 0
                        ship_hit = True
                        ship.status_update()
                        if ship.status is True:
                            damaged_cells = ((choice[0] + 1, choice[1] - 1), (choice[0] - 1, choice[1] + 1),\
                                             (choice[0] + 1, choice[1] + 1), (choice[0] - 1, choice[1] - 1))
                            for i, coordinates in enumerate(self.board.battlefield):
                                for eng_coord in damaged_cells:
                                    if eng_coord in coordinates:
                                        coordinates[eng_coord] = 0
                                        opponent_field[i][eng_coord] = 0
                            print('Computer hit the ship!')
                        elif ship.status is False:
                            print('Computer destroyed the ship!')
                            for coordinate in sorted(ship.coordinates.keys()):
                                for x in range(coordinate[0] - 1, coordinate[0] + 2):
                                    for y in range(coordinate[1] - 1, coordinate[1] + 2):
                                        for i, coordinates in enumerate(self.board.battlefield):
                                            if (x, y) in coordinates and (x, y) not in ship.coordinates:
                                                coordinates[(x, y)] = 0
                                                opponent_field[i][(x, y)] = 0
                        flag = True, True
                        break
                    elif ship.coordinates[choice] == 0:
                        choice = randint(0, 9), randint(0, 9)
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
                            print('Comp missed')
                            row[choice] = 0
                            opponent_field[i][choice] = 0
                            flag = True, True
                            break
                        elif row[choice] == 0:
                            break
        return ship_hit
