import pygame_board
import pygame_ship_class
from random import randint


class Player:
    def __init__(self, is_computer=True):
        self.is_computer = is_computer
        self.name = 'Player' if not is_computer else 'Computer'
        self.ships = [pygame_ship_class.Ship(decks) for decks in (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)]
        self.board = pygame_board.Board()
        self.ship_placement()

    def ship_placement(self):
        """ this method places all ships on the board randomly """
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
                if self.ship_placement_coordinates_validation(coordinates):
                    ship.coordinates = dict.fromkeys(coordinates, 1)
                    ship.orientation = orientation
                    ship.status
                    break

    def ship_placement_coordinates_validation(self, coordinates):
        """ this method checks if coordinates from self.ship_placement is valid """
        for ship in self.ships:
            for coordinate in coordinates:
                for x in range(coordinate[0] - 1, coordinate[0] + 2):
                    for y in range(coordinate[1] - 1, coordinate[1] + 2):
                        if (x, y) in ship.coordinates:
                            return False
        return True

    def attack(self, coordinate, opponent):
        for ship in opponent.ships:
            if coordinate in ship.coordinates:
                ship.coordinates[coordinate] = 0
                self.board.shadows_around_damaged_ship_cell(coordinate, opponent.board.field)
        else:
            self.board.battlefield[coordinate] = 0
            opponent.board.field[coordinate] = 0
            return False

    # def attack(self, coordinates, opponent_ships, opponent_field):
    #     flag = False, False
    #     ship_hit = False
    #     while True:
    #         if flag == (True, True):
    #             break
    #         else:
    #             flag = False, False
    #         choice = coordinates
    #         for ship in opponent_ships:
    #             if choice in ship.coordinates:
    #                 if ship.coordinates[choice] == 1:
    #                     ship.coordinates[choice] = 0
    #                     ship_hit = True
    #                     ship.status_update()
    #                     if ship.status is True:
    #                         damaged_cells = ((choice[0] + 1, choice[1] - 1), (choice[0] - 1, choice[1] + 1),\
    #                                          (choice[0] + 1, choice[1] + 1), (choice[0] - 1, choice[1] - 1))
    #                         for i, coordinates in enumerate(self.board.battlefield):
    #                             for eng_coord in damaged_cells:
    #                                 if eng_coord in coordinates:
    #                                     coordinates[eng_coord] = 0
    #                                     opponent_field[i][eng_coord] = 0
    #                         print('Ship is on fire!')
    #                     elif ship.status is False:
    #                         print('You destroyed the ship!')
    #                         for coordinate in sorted(ship.coordinates.keys()):
    #                             for x in range(coordinate[0] - 1, coordinate[0] + 2):
    #                                 for y in range(coordinate[1] - 1, coordinate[1] + 2):
    #                                     for i, coordinates in enumerate(self.board.battlefield):
    #                                         if (x, y) in coordinates and (x, y) not in ship.coordinates:
    #                                             coordinates[(x, y)] = 0
    #                                             opponent_field[i][(x, y)] = 0
    #                     flag = True, True
    #                     break
    #                 elif ship.coordinates[choice] == 0:
    #                     print('You already hit that cell')
    #                     flag = True, True
    #                     break
    #         if flag == (True, True):
    #             break
    #         elif flag == (True, False):
    #             continue
    #         else:
    #             for i, row in enumerate(self.board.battlefield):
    #                 if choice in row:
    #                     if row[choice] == 1:
    #                         print('You missed.')
    #                         row[choice] = 0
    #                         opponent_field[i][choice] = 0
    #                         flag = True, True
    #                         break
    #                     elif row[choice] == 0:
    #                         print('You already hit that cell')
    #                         break
    #     return ship_hit

