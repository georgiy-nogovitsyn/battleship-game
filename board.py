class Board():
    def __init__(self):
        self.size = 10
        self.clean_cell = '□'
        self.field = [[self.clean_cell] * self.size] * self.size
        self.battle_field = [[self.clean_cell] * self.size] * self.size

    def board_draw(self, positions=[]):
        print('   A B C D E F G H I J\t\t A B C D E F G H I J')
        for y in range(self.size):
            print(y, end='  ')
            for x in range(self.size):
                if (x, y) in positions:
                    print('$', end=' ')
                else:
                    print(self.field[y][x], end=' ')
            print('\t ', y, end='  ')
            for x in range(self.size):
                print(self.battle_field[y][x], end=' ')
            print()


