
ships_field = [[0 for _ in range(0,10)] for x in range(0,10)]
a = {'orientation': 0, 'decks': 3, 'x': 3, 'y': 3}

#(5, 5), 4, 0
b = [0, 3, (3, 3)]
if b[0] == 1:
    for coord in range(1, b[1]):
        b.append((b[-1][0] + 1, b[-1][-1]))
    print(b)
elif b[0] == 0:
    for coord in range(1, b[1]):
        b.append((b[-1][0], b[-1][-1] + 1))
print(b)
for i_r, x in enumerate(ships_field):
    for i_c, y in enumerate(x):
        if (i_r, i_c) in b:
            ships_field[i_r][i_c] = 1
        else:
            if b[0] == 0:
                if b[2][0] - 1 <= i_r <= b[2][0] + 1 and b[2][1] - 1 <= i_c <= b[2][1] + b[1]:
                    ships_field[i_r][i_c] = 'x'
            elif b[0] == 1:
                if b[2][0] - 1 <= i_r <= b[2][0] + b[1] and b[2][1] - 1 <= i_c <= b[2][1] + 1:
                    ships_field[i_r][i_c] = 'x'

# 5, 5, 4, 0


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

