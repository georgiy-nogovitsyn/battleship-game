class Board:
    def __init__(self):
        self.size = 10
        self.clean_cell = '□'
        self.field = [[self.clean_cell for _ in range(self.size)] for _ in range(self.size)]
        self.battle_field = [[self.clean_cell for _ in range(self.size)] for _ in range(self.size)]

    def board_draw(self):
        print('   A B C D E F G H I J\t\t A B C D E F G H I J')
        for row in range(self.size):
            print(row, end='  ')
            for cell in range(self.size):
                print(self.field[row][cell], end=' ')
            print('\t ', row, end='  ')
            for cell in range(self.size):
                print(self.battle_field[row][cell], end=' ')
            print()

user_board = Board()

user_board.board_draw()
