import pygame
from pygame_config import *


def draw_board_numbers(screen, font, color=BLACK, num_offset=5):
    # Top row of numbers for left board
    for x in range(10):
        num = str(x)
        number_font = font.render(num, True, color)
        screen.blit(number_font, (left_border_offset + num_offset + (CELL * x), top_offset - CELL))

    # Column of numbers for left board
    for x in range(10):
        num = str(x)
        number_font = font.render(num, True, color)
        screen.blit(number_font, (left_border_offset - CELL + num_offset, top_offset - 1 + (CELL * x)))


def draw_basic_board(screen):
    # Draw left board
    for x in range(10):
        for y in range(10):
            pygame.draw.rect(screen, GREY, [(CELL * x) + left_border_offset, (CELL * y) + top_offset, CELL, CELL])
            pygame.draw.rect(screen, BLACK, [(CELL * x) + left_border_offset, (CELL * y) + top_offset, CELL, CELL],
                             width=1,
                             border_radius=2)
    # Draw right board
    for x in range(10):
        for y in range(10):
            pygame.draw.rect(screen, GREY, [(CELL * x) + right_border_offset, (CELL * y) + top_offset, CELL, CELL])
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


def highlight_cell(surface, coord, border_offset=right_border_offset, top_offset=top_offset):
    """draws a rectangle on given coordinates"""
    x, y = coord
    pygame.draw.rect(surface, HIGHLIGHT_COLOR,
                     [(CELL * x) + border_offset, (CELL * y) + top_offset, CELL, CELL],
                     width=2, border_radius=3)


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Battleship Game Board")

    arial_font = pygame.font.SysFont('arial', CELL)
    number_font = arial_font.render('1', False, BLACK, GREY)
    mouse_last_pos = []
    running = True
    while running:
        screen.fill(WHITE)

        draw_basic_board(screen)
        draw_board_numbers(screen, arial_font)

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
