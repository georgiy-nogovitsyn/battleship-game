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
                self.board.shadows_around_damaged_ship(ship, coordinate, opponent)
                return True
        else:
            self.board.battlefield[coordinate] = 0
            opponent.board.field[coordinate] = 0
            return False
