from pygame_config import *
import pygame
import player
import computer

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battleship Game Board")


# ships2 = [{(1,1):1, (1,2):1}, {(1,3):1}, {(8,8):1}]


class Board:
    def __init__(self):
        self.size = 10
        self.field = [{(y, x): 1 for x in range(10)} for y in range(10)]
        self.battlefield = [{(y, x): 1 for x in range(10)} for y in range(10)]

    def check_ship(self, ships, cell):
        for ship in ships:
            if cell in ship.coordinates:
                return True
            else:
                return False

    def draw_pygame_board(self, ships, offset_x, offset_y, is_hidden=False):
        for line in self.field:
            for cell in line:
                x, y = cell
                status = line[cell]
                for ship in ships:
                    if cell in ship.coordinates:
                        status = ship.coordinates[cell]
                        if status and is_hidden:
                            cell_color = self.cell_status(status, False)
                            break
                        cell_color = self.cell_status(status, True)
                        break
                    else:
                        cell_color = self.cell_status(status, False)
                pygame.draw.rect(screen, cell_color, [(CELL * x) + offset_x, (CELL * y) + offset_y, CELL, CELL])
                pygame.draw.rect(screen, (0, 0, 0), [(CELL * x) + offset_x, (CELL * y) + offset_y, CELL, CELL], width=2,
                                 border_radius=3)

    def cell_status(self, status, if_ship):
        """status = cell status, if_ship = cell is ship or not"""
        if not if_ship:
            if status == 0:
                cell = DAMAGED_CELL
            else:
                cell = CLEAN_CELL
        else:
            if status == 0:
                cell = DAMAGED_SHIP_CELL
            else:
                cell = SHIP_CELL
        return cell

    def get_highlighted_cell_coordinate(self, mousepos):
        """Return coordinate of highlighted cell and board"""
        x, y = mousepos[0], mousepos[1]
        # if left_border_offset < x < left_border_offset + CELL * 10:
        #     if top_offset < y < top_offset + CELL * 10:
        #         pos_x, pos_y = int((x - left_border_offset) / CELL), int((y - top_offset) / CELL)
        #         return [pos_x, pos_y], 0
        if right_border_offset < x < right_border_offset + CELL * 10:
            if top_offset < y < top_offset + CELL * 10:
                pos_x, pos_y = int((x - right_border_offset) / CELL), int((y - top_offset) / CELL)
                return [pos_x, pos_y], 1

        else:
            return None

    def highlight_cell(self, coord):
        """draws a rectangle on given coordinates"""
        x, y = coord[0]

        if coord[1] == 0:  # highlight for left board
            pygame.draw.rect(screen, HIGHLIGHT_COLOR,
                             [(CELL * x) + left_border_offset, (CELL * y) + top_offset, CELL, CELL], width=2,
                             border_radius=3)

        elif coord[1] == 1:
            pygame.draw.rect(screen, HIGHLIGHT_COLOR,
                             [(CELL * x) + right_border_offset, (CELL * y) + top_offset, CELL, CELL],
                             width=2, border_radius=3)


if __name__ == '__main__':
    player = player.Player()
    player.ship_placement()

    comp = computer.Comp()
    comp.ship_placement()

    pygame_board = Board()
    mouse_last_pos = []

    running = True
    while running:
        screen.fill((255, 255, 255))

        pygame_board.draw_pygame_board(player.ships, left_border_offset, top_offset)
        pygame_board.draw_pygame_board(comp.ships, right_border_offset, top_offset, True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                mousepos = pygame.mouse.get_pos()
                highlight_coord = pygame_board.get_highlighted_cell_coordinate(mousepos)
                mouse_last_pos = highlight_coord
            if event.type == pygame.MOUSEBUTTONDOWN and mouse_last_pos:
                print('mouse pressed')

        if mouse_last_pos:  # Highlight board cell
            pygame_board.highlight_cell(mouse_last_pos)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
