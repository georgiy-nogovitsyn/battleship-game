from pygame_config import *
import pygame
pygame.init()

class Board:
    def __init__(self):
        self.size = 10
        self.field = {(y, x): 1 for x in range(self.size) for y in range(self.size)}
        self.battlefield = {(y, x): 1 for x in range(self.size) for y in range(self.size)}

    def draw_pygame_board(self, field, ships, offset_x, offset_y, is_hidden, screen):
        for cell in field:
            x, y = cell
            status = field[cell]
            for ship in ships:
                if cell in ship.coordinates:
                    status = ship.coordinates[cell]
                    cell_color = self.cell_status(status, True, is_hidden)
                    break
                else:
                    cell_color = self.cell_status(status, False, is_hidden)
            pygame.draw.rect(screen, cell_color, [(CELL * x) + offset_x, (CELL * y) + offset_y, CELL, CELL],
                             border_radius=4)
            pygame.draw.rect(screen, (0, 0, 0), [(CELL * x) + offset_x, (CELL * y) + offset_y, CELL, CELL], width=2,
                             border_radius=3)

    def cell_status(self, status, is_ship, is_hidden):
        """status = cell status, if_ship = cell is ship or not"""
        if not is_ship:
            if status == 0:
                cell = DAMAGED_CELL
            else:
                cell = CLEAN_CELL
        else:
            if status == 0:
                cell = DAMAGED_SHIP_CELL
            else:
                if is_hidden:
                    cell = CLEAN_CELL
                else:
                    cell = SHIP_CELL
        return cell

    def get_highlighted_cell_coordinate(self, mousepos):
        """Return coordinate of highlighted cell and board"""
        x, y = mousepos[0], mousepos[1]
        if right_border_offset < x < right_border_offset + CELL * 10:
            if top_offset < y < top_offset + CELL * 10:
                pos_x, pos_y = int((x - right_border_offset) / CELL), int((y - top_offset) / CELL)
                return pos_x, pos_y
        else:
            return None

    def highlight_cell(self, coord, screen):
        """draws a rectangle on given coordinates"""
        x, y = coord
        pygame.draw.rect(screen, HIGHLIGHT_COLOR,
                         [(CELL * x) + right_border_offset, (CELL * y) + top_offset, CELL, CELL],
                         width=2, border_radius=3)
    def shadows_around_damaged_ship(self, ship, attacked_coordinate, opponent):
        """ this method changes cells to damaged around damaged ship cell in attacker battlefield and attacked field """
        ship.status_update()
        if ship.status is False:
            for coordinate in sorted(ship.coordinates.keys()):
                for x in range(coordinate[0] - 1, coordinate[0] + 2):
                    for y in range(coordinate[1] - 1, coordinate[1] + 2):
                        if (x, y) in self.battlefield and (x, y) not in ship.coordinates:
                            self.battlefield[(x, y)] = 0
                            opponent.board.field[(x, y)] = 0
        else:
            for x in range(attacked_coordinate[0] - 1, attacked_coordinate[0] + 2, 2):
                for y in range(attacked_coordinate[1] - 1, attacked_coordinate[1] + 2, 2):
                    if (x, y) in self.battlefield:
                        self.battlefield[(x, y)] = 0
                        opponent.board.field[(x, y)] = 0

