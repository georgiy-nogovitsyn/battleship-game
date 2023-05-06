import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battleship Game Board")

# Colors
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Cell size
CELL = 30

# Offsets for correct rectangle drawing
left_border_offset = CELL
right_border_offset = WIDTH - CELL * 11
top_offset = CELL * 2

mouse_last_pos = []

board = []
for x in range(10):
    for y in range(10):
        board.append([[x, y], GRAY])


def draw_board(board, offset_x=0, offset_y=CELL):
    for cell in board:
        x, y = cell[0]
        color = cell[1]

        pygame.draw.rect(screen, color, [(CELL * x) + offset_x, (CELL * y) + offset_y, CELL, CELL])
    for cell in board:
        x, y = cell[0]
        pygame.draw.rect(screen, BLACK, [(CELL * x) + offset_x, (CELL * y) + offset_y, CELL, CELL], width=2,
                         border_radius=3)


def get_highlighted_cell_coordinate(mousepos):
    """Return coordinate of highlighted cell and board"""
    x, y = mousepos[0], mousepos[1]
    # if left_border_offset < x < left_border_offset + CELL * 10:
    #     if top_offset < y < top_offset + CELL * 10:
    #         pos_x, pos_y = int((x - left_border_offset) / CELL), int((y - top_offset) / CELL)
    #         return [pos_x, pos_y], 0
    if right_border_offset < x < right_border_offset + CELL * 10:
        if top_offset < y < top_offset + CELL * 10:
            pos_x, pos_y = int((x - right_border_offset) / CELL), int((y - top_offset) / CELL)
            return [pos_x, pos_y]

    else:
        return None


def highlight_cell(coord):
    """draws a rectangle on given coordinates"""
    x, y = coord

    # if coord[1] == 0:  # highlight for left board
    #     pygame.draw.rect(screen, GREEN, [(CELL * x) + left_border_offset, (CELL * y) + top_offset, CELL, CELL],
    #                      border_radius=3)

    # elif coord[1] == 1:
    pygame.draw.rect(screen, GREEN, [(CELL * x) + right_border_offset, (CELL * y) + top_offset, CELL, CELL],
                         border_radius=3)
    print(coord)


# Main game loop
running = True
while running:
    screen.fill(GRAY)

    draw_board(board, left_border_offset, top_offset)  # left board
    draw_board(board, right_border_offset, top_offset)  # right board

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            mousepos = pygame.mouse.get_pos()
            highlight_coord = get_highlighted_cell_coordinate(mousepos)
            mouse_last_pos = highlight_coord  # Save mouse position
            print(mouse_last_pos)

    if mouse_last_pos:  # Highlight board cell
        highlight_cell(mouse_last_pos)

    # Update screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
