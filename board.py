import config


class Board:
    def __init__(self):
        self.size = 10
        self.field = [{(y, x): 1 for x in range(10)} for y in range(10)] # список < словари < координаты это (x, y): 0 или 1. 0 поврежденная, 1 целая.
        self.battlefield = [{(y, x): 1 for x in range(10)} for y in range(10)]

    def draw(self, ships, opponent_ships):
        print('   0  1  2  3  4  5  6  7  8  9 \t\t 0  1  2  3  4  5  6  7  8  9')
        for i in range(self.size):
            print(i, end='  ')
            for cell in self.field[i]:
                flag = False
                for ship in ships:
                    if cell in ship.coordinates:
                        if ship.coordinates[cell] == 1:
                            print(config.SHIP_CELL, end='  ')
                        elif ship.coordinates[cell] == 0:
                            print(config.DAMAGED_SHIP_CELL, end='  ')
                        flag = True
                        break
                if flag is False:
                    if self.field[i][cell] == 1:
                        print(config.CLEAN_CELL, end='  ')
                    elif self.field[i][cell] == 0:
                        print(config.DAMAGED_CELL, end='  ')

            print(f'\t  {i}', end='  ')

            for cell in self.battlefield[i]:
                flag = False
                for ship in opponent_ships:
                    if cell in ship.coordinates:
                        if ship.coordinates[cell] == 1:
                            print(config.CLEAN_CELL, end='  ')
                        elif ship.coordinates[cell] == 0:
                            print(config.DAMAGED_SHIP_CELL, end='  ')
                        flag = True
                        break
                if flag is False:
                    if self.battlefield[i][cell] == 1:
                        print(config.CLEAN_CELL, end='  ')
                    elif self.battlefield[i][cell] == 0:
                        print(config.DAMAGED_CELL, end='  ')

            print()
