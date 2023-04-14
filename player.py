import board
import Ship
from random import randint


class Player:
    def __init__(self, computer):
        self.board = board.Board()
        self.ships = [Ship.Ship(decks) for decks in (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)]
        self.all_ships_coordinates = {}
        self.computer = computer
        if computer is True:
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
                    # for coordinate in ship.coordinates:
                    #     self.board.field.pop(coordinate)
                    #     self.board.battlefield.pop(coordinate)  # opponent battlefield
                    self.all_ships_coordinates.update(ship.coordinates)
                    break

    def attack(self, opponent_ships, opponent_field):
        if self.computer is True:
            flag = False
            while True:
                choice = randint(0, 9), randint(0, 9)
                for ship in opponent_ships:
                    if choice in ship.coordinates:
                        if ship.coordinates[choice] == 1:
                            ship.coordinates[choice] = 0
                            print(f'get the ship {choice}')
                            flag = True
                            break
                        elif ship.coordinates[choice] == 0:
                            choice = randint(0, 9), randint(0, 9)
                if flag:
                    break
                else:
                    if self.board.battlefield[choice] == 1:
                        print(f'missed {choice}')
                        self.board.battlefield[choice] = 0
                        opponent_field[choice] = 0
                        break


player = Player(False)
comp = Player(True)
player.ship_placement()
# player.board.draw(player.ships)
# player.board.draw_new(player.ships)
for _ in range(25):
    comp.attack(player.ships, player.board.field)
player.board.draw_new(player.ships, comp.ships)
comp.board.draw_new(comp.ships, player.ships)
# [-1][-1]     [-1][+1]
#         0 0 0
#         0 x 0
#         0 0 0
# [+1][-1]     [+1][+1]
