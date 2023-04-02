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

ships_field = [[0 for _ in range(0,10)] for x in range(0,10)]
def fields_draw(ships_field):
    print('   A B C D E F G H I J\t\t   A B C D E F G H I J')
    for x in range(0, 10):
        print(x, end='  ')
        for ch in ships_field[x]:
            print(ch, end=' ')
        print('\t' * 2, end='')
        print(x, end='  ')
        for ch in ships_field[x]:
            print(ch, end=' ')
        print()
fields_draw(ships_field)
#(5, 5), 4, 0
#(4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9)
for i_r, row in enumerate(ships_field):
    for i_c, column in enumerate(row):
        pass

# 5, 5, 4, 0
b = [0, 4, [5, 5]]

for x in range(b[1]-1):
    new = b[-1][0]+1,b[-1][1]
    b.append(list(new))

print(b)

