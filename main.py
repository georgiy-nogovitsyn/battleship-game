import random

field_cell = '□'
ship_symbol = 'S'
damaged_ship_symbol = 'D'
engaged_cell_symbol = '*'

user1_ships_field = [[field_cell for _ in range(0, 10)] for _ in range(0, 10)]
user1_battle_field = [[field_cell for _ in range(0, 10)] for _ in range(0, 10)]
computer_ships_field = [[field_cell for _ in range(0, 10)] for _ in range(0, 10)]
computer_battle_field = [[field_cell for _ in range(0, 10)] for _ in range(0, 10)]

# that function draws two fields
def fields_draw(ships_field, battle_field):
    print('   A B C D E F G H I J\t\t   A B C D E F G H I J')
    for x in range(0, 10):
        print(x, end='  ')
        for ch in ships_field[x]:
            print(ch, end=' ')
        print('\t' * 2, end='')
        print(x, end='  ')
        for ch in battle_field[x]:
            print(ch, end=' ')
        print()


def field_cleaner(ships_field):
    for counter, x in enumerate(ships_field):
        for index, y in enumerate(x):
            if y == engaged_cell_symbol:
                ships_field[counter][index] = field_cell


# that function places ships on the field properly
def ship_placement(ships_field, decks_num, orient, y_coord, x_coord):
    global ship_symbol
    global engaged_cell_symbol
    ship_placement_status = False
    if coords_validation(ships_field, decks_num, orient, y_coord, x_coord) is True:
        # horizontal
        if orient == 0:
            ships_field[y_coord][x_coord:x_coord + decks_num] = ship_symbol * decks_num
            # without borders
            if 0 < y_coord < 9 and 0 < x_coord and x_coord + (decks_num - 1) < 9:
                ships_field[y_coord - 1][x_coord - 1:x_coord + decks_num + 1] = engaged_cell_symbol * (decks_num + 2)
                ships_field[y_coord + 1][x_coord - 1:x_coord + decks_num + 1] = engaged_cell_symbol * (decks_num + 2)
                ships_field[y_coord][x_coord - 1] = engaged_cell_symbol
                ships_field[y_coord][x_coord + decks_num] = engaged_cell_symbol
            # left border
            elif 0 < y_coord < 9 and 0 == x_coord:
                ships_field[y_coord - 1][x_coord:x_coord + decks_num + 1] = engaged_cell_symbol * (decks_num + 1)
                ships_field[y_coord + 1][x_coord:x_coord + decks_num + 1] = engaged_cell_symbol * (decks_num + 1)
                ships_field[y_coord][x_coord + decks_num] = engaged_cell_symbol
            # right border
            elif 0 < y_coord < 9 and x_coord + (decks_num - 1) == 9:
                ships_field[y_coord - 1][x_coord - 1:x_coord + decks_num] = engaged_cell_symbol * (decks_num + 1)
                ships_field[y_coord + 1][x_coord - 1:x_coord + decks_num] = engaged_cell_symbol * (decks_num + 1)
                ships_field[y_coord][x_coord - 1] = engaged_cell_symbol
            # top border
            elif y_coord == 0 and 0 < x_coord and x_coord + (decks_num - 1) < 9:
                ships_field[y_coord + 1][x_coord - 1:x_coord + decks_num + 1] = engaged_cell_symbol * (decks_num + 2)
                ships_field[y_coord][x_coord - 1] = engaged_cell_symbol
                ships_field[y_coord][x_coord + decks_num] = engaged_cell_symbol
            # bottom border
            elif y_coord == 9 and 0 < x_coord and x_coord + (decks_num - 1) < 9:
                ships_field[y_coord - 1][x_coord - 1:x_coord + decks_num + 1] = engaged_cell_symbol * (decks_num + 2)
                ships_field[y_coord][x_coord - 1] = engaged_cell_symbol
                ships_field[y_coord][x_coord + decks_num] = engaged_cell_symbol
            # top left border
            elif y_coord == 0 and x_coord == 0:
                ships_field[y_coord + 1][x_coord:x_coord + decks_num + 1] = engaged_cell_symbol * (decks_num + 1)
                ships_field[y_coord][x_coord + decks_num] = engaged_cell_symbol
            # top right border
            elif y_coord == 0 and x_coord + (decks_num - 1) == 9:
                ships_field[y_coord + 1][x_coord - 1:x_coord + decks_num] = engaged_cell_symbol * (decks_num + 1)
                ships_field[y_coord][x_coord - 1] = engaged_cell_symbol
            # bottom left border
            elif y_coord == 9 and x_coord == 0:
                ships_field[y_coord - 1][x_coord:x_coord + decks_num + 1] = engaged_cell_symbol * (decks_num + 1)
                ships_field[y_coord][x_coord + decks_num] = engaged_cell_symbol
            # bottom right border
            elif y_coord == 9 and x_coord + (decks_num - 1) == 9:
                ships_field[y_coord - 1][x_coord - 1:x_coord + decks_num] = engaged_cell_symbol * (decks_num + 1)
                ships_field[y_coord][x_coord - 1] = engaged_cell_symbol
        # y - vertical, x - horizontal
        # vertical
        elif orient == 1:
            for _ in range(y_coord, y_coord + decks_num):
                ships_field[_][x_coord] = ship_symbol
            # without borders
            if 0 < y_coord and (y_coord + decks_num - 1) < 9 and 0 < x_coord < 9:
                for _ in range(y_coord - 1, y_coord + decks_num + 1):
                    ships_field[_][x_coord - 1] = engaged_cell_symbol
                for _ in range(y_coord - 1, y_coord + decks_num + 1):
                    ships_field[_][x_coord + 1] = engaged_cell_symbol
                ships_field[y_coord - 1][x_coord] = engaged_cell_symbol
                ships_field[y_coord + decks_num][x_coord] = engaged_cell_symbol
            # left border
            elif y_coord > 0 == x_coord and (y_coord + decks_num - 1) != 9:
                for _ in range(y_coord - 1, y_coord + decks_num + 1):
                    ships_field[_][x_coord + 1] = engaged_cell_symbol
                ships_field[y_coord - 1][x_coord] = engaged_cell_symbol
                ships_field[y_coord + decks_num][x_coord] = engaged_cell_symbol
            # right border
            elif 0 < y_coord and (y_coord + decks_num - 1) != 9 and x_coord == 9:
                for _ in range(y_coord - 1, y_coord + decks_num + 1):
                    ships_field[_][x_coord - 1] = engaged_cell_symbol
                ships_field[y_coord - 1][x_coord] = engaged_cell_symbol
                ships_field[y_coord + decks_num][x_coord] = engaged_cell_symbol
            # top border
            elif y_coord == 0 and 0 < x_coord < 9:
                for _ in range(y_coord, y_coord + decks_num + 1):
                    ships_field[_][x_coord - 1] = engaged_cell_symbol
                for _ in range(y_coord, y_coord + decks_num + 1):
                    ships_field[_][x_coord + 1] = engaged_cell_symbol
                ships_field[y_coord + decks_num][x_coord] = engaged_cell_symbol
            # bottom border
            if (y_coord + decks_num - 1) == 9 and 0 < x_coord < 9:
                for _ in range(y_coord - 1, y_coord + decks_num):
                    ships_field[_][x_coord - 1] = engaged_cell_symbol
                for _ in range(y_coord - 1, y_coord + decks_num):
                    ships_field[_][x_coord + 1] = engaged_cell_symbol
                ships_field[y_coord - 1][x_coord] = engaged_cell_symbol
            # top left border
            elif y_coord == 0 and x_coord == 0:
                for _ in range(y_coord, y_coord + decks_num + 1):
                    ships_field[_][x_coord + 1] = engaged_cell_symbol
                ships_field[y_coord + decks_num][x_coord] = engaged_cell_symbol
            # top right border
            elif y_coord == 0 and x_coord == 9:
                for _ in range(y_coord, y_coord + decks_num + 1):
                    ships_field[_][x_coord - 1] = engaged_cell_symbol
                ships_field[y_coord + decks_num][x_coord] = engaged_cell_symbol
            # bottom left border
            elif (y_coord + decks_num - 1) == 9 and x_coord == 0:
                for _ in range(y_coord - 1, y_coord + decks_num):
                    ships_field[_][x_coord + 1] = engaged_cell_symbol
                ships_field[y_coord - 1][x_coord] = engaged_cell_symbol

            # bottom right border
            elif (y_coord + decks_num - 1) == 9 and x_coord == 9:
                for _ in range(y_coord - 1, y_coord + decks_num):
                    ships_field[_][x_coord - 1] = engaged_cell_symbol
                ships_field[y_coord - 1][x_coord] = engaged_cell_symbol

    else:
        pass
    return ship_placement_status


# that function validates ships placement (checks if cell is already taken and if ship goes out of the field borders)
def coords_validation(ships_field, decks_num, orient, y_coord, x_coord):
    validation_result = False
    global ship_symbol
    global engaged_cell_symbol
    if orient == 0:
        if (x_coord + decks_num - 1) <= 9:
            if ship_symbol not in ships_field[y_coord][x_coord:x_coord + decks_num] and engaged_cell_symbol not in \
                    ships_field[
                        y_coord][
                    x_coord:x_coord + decks_num]:
                validation_result = True
            else:
                pass
                # print('That cell is already taken by another ship')
        else:
            pass
            # print('The ship goes out of the field\'s border')
    elif orient == 1:
        if y_coord + decks_num - 1 <= 9:
            li_checker = []
            for _ in range(y_coord, y_coord + decks_num):
                li_checker.append(ships_field[_][x_coord])
            if ship_symbol not in li_checker and engaged_cell_symbol not in li_checker:
                validation_result = True
            else:
                pass
                # print('That cell is already taken by another ship')
        else:
            pass
            # print('The ship goes out of the field\'s border')
    return validation_result


def random_ship_placement(ships_field, battle_field):
    decks_quantity = {'4': 1, '3': 2, '2': 3, '1': 4}
    while sum(decks_quantity.values()) > 0:
        decks_num = random.choice(list(decks_quantity.keys()))
        while decks_quantity[decks_num] <= 0:
            decks_num = random.choice(list(decks_quantity.keys()))
        orient = random.randrange(0, 2)
        y_coord = random.randrange(0, 10)
        x_coord = random.randrange(0, 10)
        while not coords_validation(ships_field, int(decks_num), orient, y_coord, x_coord):
            orient = random.randrange(0, 2)
            y_coord = random.randrange(0, 10)
            x_coord = random.randrange(0, 10)
        ship_placement(ships_field, int(decks_num), orient, y_coord, x_coord)
        decks_quantity[decks_num] -= 1

    fields_draw(ships_field, battle_field)

    approve = input('Do you wanna change placement?\ty/n\n')
    if approve != 'n':
        ships_field = [[field_cell for _ in range(0, 10)] for _ in range(0, 10)]
        random_ship_placement(ships_field, battle_field)


def random_ship_placement_computer(ships_field):
    decks_quantity = {'4': 1, '3': 2, '2': 3, '1': 4}
    while sum(decks_quantity.values()) > 0:
        decks_num = random.choice(list(decks_quantity.keys()))
        while decks_quantity[decks_num] <= 0:
            decks_num = random.choice(list(decks_quantity.keys()))
        orient = random.randrange(0, 2)
        y_coord = random.randrange(0, 10)
        x_coord = random.randrange(0, 10)
        while not coords_validation(ships_field, int(decks_num), orient, y_coord, x_coord):
            orient = random.randrange(0, 2)
            y_coord = random.randrange(0, 10)
            x_coord = random.randrange(0, 10)
        ship_placement(ships_field, int(decks_num), orient, y_coord, x_coord)
        decks_quantity[decks_num] -= 1


def manual_ship_placement(ships_field, battle_field):
    decks_quantity = {'4': 1, '3': 2, '2': 3, '1': 4}

    while sum(list(decks_quantity.values())) > 0:
        fields_draw(ships_field, battle_field)
        while True:
            try:
                print(decks_quantity)
                decks_num = int(input('Choose decks number (1-4): '))
                if decks_num in [1, 2, 3, 4]:
                    if decks_quantity[str(decks_num)] > 0:
                        decks_quantity[str(decks_num)] -= 1
                        break
                    else:
                        print('You don\'t have decks of that quantity.')
                else:
                    print('Only integers from 1 to 4.')
            except ValueError:
                print('Only integers from 1 to 4.')
        while True:
            try:
                orient = int(input('Choose orientation of the ship: 0 for horizontal, 1 for vertical: '))
                if orient in [0, 1]:
                    break
                else:
                    print('Only 0 and 1 integers allow')
            except ValueError:
                print('Only 0 and 1 integers allow.')
        while True:
            try:
                xy_coord = input('Choose coordinates: A-J for columns and 0-9 for rows (e.g. B5): ')
                x_coord, y_coord = xy_coord[0].upper(), int(xy_coord[1])

                if x_coord in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J') and y_coord in [num for num in
                                                                                                 range(0, 10)]:
                    x_coord_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
                    x_coord = x_coord_dict[x_coord]
                    if coords_validation(ships_field, decks_num, orient, y_coord, x_coord) is True:
                        ship_placement(ships_field, decks_num, orient, y_coord, x_coord)
                        quit()
                    else:
                        print('You can\'t place here, probably there\'s another ship already placed')
                else:
                    print('Uh-oh, you\'ve made a mistake')
            except ValueError:
                print('Only 0 and 1 integers allow.')


def cells_around_dmg_ship(battle_field, y_coord, x_coord):

    if 0 < y_coord < 9 and 0 < x_coord < 9:
        battle_field[y_coord - 1][x_coord - 1:x_coord + 2:2] = engaged_cell_symbol * 2
        battle_field[y_coord + 1][x_coord - 1:x_coord + 2:2] = engaged_cell_symbol * 2
    elif 9 > y_coord > 0 == x_coord:
        battle_field[y_coord - 1][x_coord + 1] = engaged_cell_symbol
        battle_field[y_coord + 1][x_coord + 1] = engaged_cell_symbol
    elif y_coord == 0 and x_coord == 0:
        battle_field[y_coord + 1][x_coord + 1] = engaged_cell_symbol
    elif y_coord == 0 and x_coord == 9:
        battle_field[y_coord + 1][x_coord - 1] = engaged_cell_symbol
    elif y_coord == 0 and 0 < x_coord < 9:
        battle_field[y_coord + 1][x_coord - 1:x_coord + 2:2] = engaged_cell_symbol * 2
    elif y_coord == 9 and x_coord == 0:
        battle_field[y_coord - 1][x_coord + 1] = engaged_cell_symbol
    elif y_coord == 9 and 0 < x_coord < 9:
        battle_field[y_coord - 1][x_coord - 1:x_coord + 2:2] = engaged_cell_symbol * 2
    elif y_coord == 9 and x_coord == 9:
        battle_field[y_coord - 1][x_coord - 1] = engaged_cell_symbol
    elif 0 < y_coord < 9 and x_coord == 9:
        battle_field[y_coord - 1][x_coord - 1] = engaged_cell_symbol
        battle_field[y_coord + 1][x_coord - 1] = engaged_cell_symbol


def computer_plays(ships_field, battle_field):
    print('Computer thinking!')
    while True:
        y_coord, x_coord = random.randrange(0, 10), random.randrange(0, 10)
        if battle_field[y_coord][x_coord] == field_cell:
            break
    if ships_field[y_coord][x_coord] == ship_symbol:
        battle_field[y_coord][x_coord] = damaged_ship_symbol
        ships_field[y_coord][x_coord] = damaged_ship_symbol
        cells_around_dmg_ship(battle_field, y_coord, x_coord)
        print('Computer hit!')
        if win_checker(ships_field) is False:
            print('#############\n\nComputer won!\n\n#############')
            return False
        else:
            computer_plays(ships_field, battle_field)
    else:
        ships_field[y_coord][x_coord] = engaged_cell_symbol
        print('Computer miss!')


def user_plays(enemy_ships_field, user_ships_field, battle_field):
    while True:
        xy_coord = input('Choose coordinates: A-J for columns and 0-9 for rows AND ATTACK: ')
        if len(xy_coord) != 2:
            print('You made a mistake with coordinates.')
        elif xy_coord[0].upper() not in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'):
            print('You made a mistake with coordinates.')
        elif xy_coord[1] not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            print('You made a mistake with coordinates.')
        else:
            x_coord, y_coord = xy_coord[0].upper(), int(xy_coord[1])
            x_coord_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
            x_coord = x_coord_dict[x_coord]
            if battle_field[y_coord][x_coord] != field_cell:
                print('You can\'t choose that cell')
            else:
                break

    if enemy_ships_field[y_coord][x_coord] == ship_symbol:
        battle_field[y_coord][x_coord] = damaged_ship_symbol
        cells_around_dmg_ship(battle_field, y_coord, x_coord)
        enemy_ships_field[y_coord][x_coord] = damaged_ship_symbol
        print('Hit!')
        fields_draw(user_ships_field, battle_field)
        if win_checker(enemy_ships_field) is False:
            print('########\n\nYou won!\n\n########')
            return False
        else:
            user_plays(enemy_ships_field, user_ships_field, battle_field)
    else:
        battle_field[y_coord][x_coord] = engaged_cell_symbol
        print('Miss!')

def win_checker(ships_field):
    for x in ships_field:
        if ship_symbol in x:
            return True
    return False


def game():
    random_ship_placement(user1_ships_field, user1_battle_field)
    random_ship_placement_computer(computer_ships_field)
    field_cleaner(user1_ships_field)
    while True:
        if user_plays(computer_ships_field, user1_ships_field, user1_battle_field) is False:
            break
        fields_draw(user1_ships_field, user1_battle_field)

        if computer_plays(user1_ships_field, computer_battle_field) is False:
            break
        fields_draw(user1_ships_field, user1_battle_field)


game()
