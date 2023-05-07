from pygame_config import *
import pygame
import pygame_player, pygame_computer, pygame_utils
pygame.init()
clock = pygame.time.Clock()


# Set up the game window
WIDTH = 800
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battleship Game Board")

# Cell size
CELL = 30

# Offsets for correct rectangle drawing
left_border_offset = CELL
right_border_offset = WIDTH - CELL * 11
top_offset = CELL
player = pygame_player.Player()
comp = pygame_computer.Comp()
player.ship_placement()


# ships2 = [{(1,1):1, (1,2):1}, {(1,3):1}, {(8,8):1}]


class Board:
    def __init__(self):
        self.size = 10
        self.field = [{(y, x): 1 for x in range(10)} for y in range(10)]
        self.battlefield = [{(y, x): 1 for x in range(10)} for y in range(10)]

    def draw_pygame_board(self, field, ships, offset_x, offset_y, is_hidden):
        for line in field:
            for cell in line:
                x, y = cell
                status = line[cell]
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
        # if left_border_offset < x < left_border_offset + CELL * 10:
        #     if top_offset < y < top_offset + CELL * 10:
        #         pos_x, pos_y = int((x - left_border_offset) / CELL), int((y - top_offset) / CELL)
        #         return [pos_x, pos_y], 0
        if right_border_offset < x < right_border_offset + CELL * 10:
            if top_offset < y < top_offset + CELL * 10:
                pos_x, pos_y = int((x - right_border_offset) / CELL), int((y - top_offset) / CELL)
                return pos_x, pos_y
        else:
            return None

    def highlight_cell(self, coord):
        """draws a rectangle on given coordinates"""
        x, y = coord
        pygame.draw.rect(screen, HIGHLIGHT_COLOR,
                         [(CELL * x) + right_border_offset, (CELL * y) + top_offset, CELL, CELL],
                         width=2, border_radius=3)


if __name__ == '__main__':
    pygame_board = Board()
    mouse_last_pos = []

    running = True
    move = True
    winner = 'Bye!'
    while running:
        move = True
        while move:
            screen.fill((255, 255, 255))
            pygame_board.draw_pygame_board(player.board.field, player.ships, left_border_offset, top_offset,
                                           False)
            pygame_board.draw_pygame_board(player.board.battlefield, comp.ships, right_border_offset,
                                           top_offset, True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    highlight_coord = pygame_board.get_highlighted_cell_coordinate(mouse_pos)
                    if highlight_coord:
                        mouse_last_pos = highlight_coord
                if event.type == pygame.MOUSEBUTTONDOWN and mouse_last_pos:
                    if pygame_utils.get_ship_index(mouse_last_pos, comp.ships):
                        player.attack(mouse_last_pos, comp.ships, comp.board.field)
                        for ship in comp.ships:
                            ship.status_update()
                            if ship.status is True:
                                running = True
                                break
                            else:
                                running = False
                                winner = 'Player'
                    elif pygame_utils.get_ship_index(mouse_last_pos, comp.ships) is False:
                        print('You already hit that ship')
                    elif pygame_utils.get_ship_index(mouse_last_pos, comp.ships) is None:
                        if player.board.battlefield[mouse_last_pos[0]][mouse_last_pos] == 1:
                            player.board.battlefield[mouse_last_pos[0]][mouse_last_pos] = 0
                            comp.board.field[mouse_last_pos[0]][mouse_last_pos] = 0
                            print('You missed')
                            move = False
                        else:
                            print('You already hit that cell')
                # ship_hit = True
                # while ship_hit:
                #     for row in player.board.battlefield:
                #         if mouse_last_pos in row and row[mouse_last_pos] == 1:
                #             if player.attack(mouse_last_pos, comp.ships, comp.board.field) is True:
                #                 ship_hit = True
                #                 for ship in comp.ships:
                #                     ship.status_update()
                #                     if ship.status is True:
                #                         running = True
                #                         break
                #                     else:
                #                         running = False
                #                         winner = 'Player'
                #             else:
                #                 ship_hit = False
                #         else:
                #             print('You already hit that cell')

                if mouse_last_pos:  # Highlight board cell
                    pygame_board.highlight_cell(mouse_last_pos)

            pygame.display.flip()
            clock.tick(30)
        move = True
        while move:
            if comp.attack(player.ships, player.board.field) is True:
                for ship in player.ships:
                    ship.status_update()
                    if ship.status is True:
                        running = True
                        break
                    else:
                        running = False
                        winner = 'Comp'
            else:
                move = False

    print(f'{winner}')

    pygame.quit()
