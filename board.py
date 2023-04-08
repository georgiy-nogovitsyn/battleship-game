class Board:
    def __init__(self):
        self.size = 10
        self.clean_cell = '□'
        self.fld = []
        for y in range(10):
            for x in range(10):
                self.fld.append((x, y))
        self.field = [[self.clean_cell] * self.size] * self.size
        self.battle_field = [[self.clean_cell] * self.size] * self.size

    def board_draw(self, positions={}):
        print('   A  B  C  D  E  F  G  H  I  J \t\t A  B  C  D  E  F  G  H  I  J')
        for y in range(self.size):
            print(y, end='  ')
            for x in range(self.size):
                if (x, y) in positions:
                    print('$', end='  ')
                else:
                    print(self.field[y][x], end='  ')
            print('\t ', y, end='  ')
            for x in range(self.size):
                print(self.battle_field[y][x], end='  ')
            print()

    def board_print(self, ships):
        print('   A  B  C  D  E  F  G  H  I  J \t\t A  B  C  D  E  F  G  H  I  J')
        for y in range(self.size):
            print(y, end='  ')
            for x in range(self.size):
                for ship in ships:
                    if (x, y) in ship.coordinates:
                        for coordinate in ship.coordinates:
                            if (x, y) == coordinate:
                                if (x+1) % 10 == 0:
                                    print('s')
                                    break
                                else:
                                    print('s', end='  ')
                                    break
                if (x, y) in self.fld:
                    for coordinate in self.fld:
                        if (x, y) == coordinate:
                            if (x+1) % 10 == 0:
                                print(self.clean_cell)
                                break
                            else:
                                print(self.clean_cell, end='  ')
                                break
