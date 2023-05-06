from pygame_config import *
import pygame

pygame.init()

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

ships = [{(0,0):1, (0,1):1}, {(2,5):1}, {(8,8):1}]
ships2 = [{(1,1):1, (1,2):1}, {(1,3):1}, {(8,8):1}]

class Board:
    def __init__(self):
        self.size = 10
        self.field = [{(y, x): 1 for x in range(10)} for y in range(10)]
        self.battlefield = [{(y, x): 1 for x in range(10)} for y in range(10)]

    def draw_pygame_board(self,ships, offset_x,offset_y):
        for line in self.field:
            for cell in line:
                y, x = cell
                status = line[cell]
                for ship in ships:
                    if cell in ship:
                        status = ship[cell]
                        cell_color = self.cell_status(status, True)
                        break
                    else:
                        cell_color = self.cell_status(status,False)
                pygame.draw.rect(screen, cell_color, [(CELL * x) + offset_x, (CELL * y) + offset_y, CELL, CELL])
                pygame.draw.rect(screen, (0,0,0), [(CELL * x) + offset_x, (CELL * y) + offset_y, CELL, CELL], width=2,
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



if __name__ == '__main__':
    pygame_board = Board()

    running = True
    while running:
        screen.fill((255,255,255))

        pygame_board.draw_pygame_board(ships,left_border_offset,top_offset)
        pygame_board.draw_pygame_board(ships2,right_border_offset,top_offset)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()
