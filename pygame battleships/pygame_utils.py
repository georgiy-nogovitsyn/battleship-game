import pygame
from pygame_config import *
import pygame_player


def draw_board_numbers(screen, font, color=BLACK, num_offset=5, offset = left_border_offset):
    # Top row of numbers for left board
    for x in range(10):
        num = str(x)
        number_font = font.render(num, True, color)
        screen.blit(number_font, (offset + num_offset + (CELL * x), top_offset - CELL))

    # Column of numbers for left board
    for x in range(10):
        num = str(x)
        number_font = font.render(num, True, color)
        screen.blit(number_font, (offset - CELL + num_offset, top_offset - 1 + (CELL * x)))


def draw_basic_board(screen):
    # Draw left board
    for x in range(10):
        for y in range(10):
            pygame.draw.rect(screen, BACKGROUND_COLOR,
                             [(CELL * x) + left_border_offset, (CELL * y) + top_offset, CELL, CELL])
            pygame.draw.rect(screen, BLACK, [(CELL * x) + left_border_offset, (CELL * y) + top_offset, CELL, CELL],
                             width=1,
                             border_radius=2)
    # Draw right board
    for x in range(10):
        for y in range(10):
            pygame.draw.rect(screen, BACKGROUND_COLOR,
                             [(CELL * x) + right_border_offset, (CELL * y) + top_offset, CELL, CELL])
            pygame.draw.rect(screen, BLACK, [(CELL * x) + right_border_offset, (CELL * y) + top_offset, CELL, CELL],
                             width=1,
                             border_radius=2)

    # Draw line around left and right boards
    pygame.draw.rect(screen, BLACK, [left_border_offset - 1, top_offset - 1, CELL * 10 + 2, CELL * 10 + 2],
                     width=2,
                     border_radius=3)
    pygame.draw.rect(screen, BLACK, [right_border_offset - 1, top_offset - 1, CELL * 10 + 2, CELL * 10 + 2],
                     width=2,
                     border_radius=3)


def get_highlighted_cell_coordinate(mousepos, offset=right_border_offset, top_offset=top_offset):
    """Return coordinate of highlighted cell on board by given offsets.
    By default returns coordinates for right border"""
    x, y = mousepos
    if offset < x < offset + CELL * 10:
        if top_offset < y < top_offset + CELL * 10:
            pos_x, pos_y = int((x - offset) / CELL), int((y - top_offset) / CELL)
            return pos_x, pos_y


def get_ship_index(coordinate, ships):
    for index, ship in enumerate(ships):
        if coordinate in ship.coordinates:
            if ship.coordinates[coordinate]:
                print(index)
                return str(index)
            else:
                return False


def highlight_cell(surface, coord, border_offset=right_border_offset, top_offset=top_offset):
    """draws a rectangle on given coordinates"""
    x, y = coord
    pygame.draw.rect(surface, HIGHLIGHT_COLOR,
                     [(CELL * x) + border_offset, (CELL * y) + top_offset, CELL, CELL],
                     width=2, border_radius=3)


def choose_ship_color(status):
    if status == 0:
        cell = DAMAGED_SHIP_CELL
    else:
        cell = SHIP_CELL
    return cell


def draw_ships(screen, ships, offset_x=left_border_offset, offset_y=top_offset, hidden = False):
    """Draws ships on board. If hidden = True draws only damaged cells on the right board"""
    if hidden:
        offset_x = right_border_offset
    for ship_cells in ships:
        coordinates = ship_cells.coordinates
        for cell in coordinates:
            x, y = cell
            status = coordinates[cell]
            cell_color = choose_ship_color(status)

            if not hidden or cell_color == DAMAGED_SHIP_CELL or cell_color == WATER_HIT:
                pygame.draw.rect(screen, cell_color, [(CELL * x) + offset_x, (CELL * y) + offset_y, CELL, CELL])
                pygame.draw.rect(screen, (0, 0, 0), [(CELL * x) + offset_x, (CELL * y) + offset_y, CELL, CELL], width=2,
                                 border_radius=3)

def draw_water_hits(screen, field, offset_x = left_border_offset, offset_y = top_offset, cell_color = WATER_HIT):
    for cell in field:
        x, y = cell
        status = field[cell]
        if status == 0: # Draw only for damaged field
            pygame.draw.rect(screen, cell_color, [(CELL * x) + offset_x, (CELL * y) + offset_y, CELL, CELL],
                             border_radius=4)
            pygame.draw.rect(screen, (0, 0, 0), [(CELL * x) + offset_x, (CELL * y) + offset_y, CELL, CELL], width=2,
                             border_radius=3)


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Battleship Game Board")

    arial_font = pygame.font.SysFont('arial', CELL)
    number_font = arial_font.render('1', False, BLACK, GREY)

    mouse_last_pos = []

    player = pygame_player.Player(False)
    comp = pygame_player.Player()

    running = True
    while running:
        screen.fill(WHITE)

        draw_basic_board(screen)
        draw_board_numbers(screen, arial_font)
        draw_ships(screen, player.ships)
        draw_ships(screen,comp.ships, hidden=True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                mousepos = pygame.mouse.get_pos()
                print(get_highlighted_cell_coordinate(mousepos))

                mouse_last_pos = get_highlighted_cell_coordinate(mousepos)

        if mouse_last_pos:
            highlight_cell(screen, mouse_last_pos)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
