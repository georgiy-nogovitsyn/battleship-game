import config


class Board:
    def __init__(self):
        self.size = 10
        self.field = dict.fromkeys([(y, x) for y in range(10) for x in range(10)], 1)
        self.battlefield = dict.fromkeys([(y, x) for y in range(10) for x in range(10)], 1)

    def draw_new(self, ships, opponent_ships):
        print('   0  1  2  3  4  5  6  7  8  9 \t\t 0  1  2  3  4  5  6  7  8  9')
        for y in range(self.size):
            print(y, end='  ')
            for x in range(self.size):
                flag = False
                for ship in ships:
                    if flag:
                        break
                    for coordinate in ship.coordinates:
                        if flag:
                            break
                        if (y, x) == coordinate:
                            if ship.coordinates[(y, x)] == 1:
                                print(config.SHIP_CELL, end='  ')
                            elif ship.coordinates[(y, x)] == 0:
                                print(config.DAMAGED_SHIP_CELL, end='  ')
                            flag = True
                if not flag:
                    for coordinate in self.field:
                        if coordinate == (y, x):
                            if self.field[(y, x)] == 1:
                                print(config.CLEAN_CELL, end='  ')
                            elif self.field[(y, x)] == 0:
                                print(config.DAMAGED_CELL, end='  ')
                            flag = True
                            break

            print(f'\t  {y}', end='  ')

            for x in range(self.size):
                flag = False
                for ship in opponent_ships:  # opp ships
                    if flag:
                        break
                    for coordinate in ship.coordinates:
                        if flag:
                            break
                        if (y, x) == coordinate:
                            if ship.coordinates[(y, x)] == 1:
                                print(config.CLEAN_CELL, end='  ')
                            elif ship.coordinates[(y, x)] == 0:
                                print(config.DAMAGED_SHIP_CELL, end='  ')
                            flag = True
                if not flag:
                    for coordinate in self.battlefield:
                        if coordinate == (y, x):
                            if self.battlefield[(y, x)] == 1:
                                print(config.CLEAN_CELL, end='  ')
                            elif self.battlefield[(y, x)] == 0:
                                print(config.DAMAGED_CELL, end='  ')
                            flag = True
                            break
            print()

    def draw(self, ships):
        print('   A  B  C  D  E  F  G  H  I  J \t\t A  B  C  D  E  F  G  H  I  J')
        for y in range(self.size):
            print(y, end='  ')
            for x in range(self.size):
                for ship in ships:
                    if (y, x) in ship.coordinates:
                        if ship.coordinates[(y, x)] == 1:
                            print(config.SHIP_CELL, end='  ')
                        else:
                            print(config.DAMAGED_SHIP_CELL, end='  ')
                if (y, x) in self.field:
                    if self.field[(y, x)] == 1:
                        print(config.CLEAN_CELL, end='  ')
                    else:
                        print(config.DAMAGED_CELL, end='  ')

            print(f'\t  {y}', end='  ')

            for x in range(self.size):  # have to re-write
                for ship in ships: #opponent ships
                    if (y, x) in ship.coordinates:
                        if ship.coordinates[(y, x)] == 1:
                            print(config.CLEAN_CELL, end='  ')
                        else:
                            print(config.DAMAGED_SHIP_CELL, end='  ')
                if (y, x) in self.battlefield:
                    if self.battlefield[(y, x)] == 1:
                        print(config.CLEAN_CELL, end='  ')
                    else:
                        print(config.DAMAGED_CELL, end='  ')
            print()
