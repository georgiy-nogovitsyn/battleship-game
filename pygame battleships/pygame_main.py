import pygame_board, pygame_computer, pygame_player, pygame_utils
import pygame
from pygame_config import *

from random import randint
pygame.init()
clock = pygame.time.Clock()

# Set up the game window
WIDTH = WIDTH
HEIGHT = HEIGHT
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battleship Game Board")

# Cell size
CELL = 30

# Offsets for correct rectangle drawing
left_border_offset = CELL
right_border_offset = WIDTH - CELL * 11
top_offset = CELL

class Game:
    def __init__(self, mode=0):
        if mode == 0:
            self.player = pygame_player.Player(False)
            self.comp = pygame_player.Player()

    def chosen_coordinate_validation(self, coordinate, attacker, opponent):
        """ validation of chosen to attack coordinate """
        if attacker.board.battlefield[coordinate] == 0:
            return False
        else:
            for ship in opponent.ships:
                if coordinate in ship.coordinates and ship.coordinates[coordinate] == 0:
                    return False
        return True

    def ships_status_update(self, ships):
        """ ships status update after hit """
        for ship in ships:
            ship.status_update()
            if ship.status is True:
                return False
            else:
                return True
    def computer_choice(self, attacker, opponent):
        while True:
            choice = randint(0, 9), randint(0, 9)
            if self.chosen_coordinate_validation(choice, attacker, opponent):
                return choice
    def start(self):
        if __name__ == '__main__':
            mouse_last_pos = []
            running = True
            winner = 'Bye!'
            while running:
                move = True
                while move and running:
                    screen.fill((255, 255, 255))
                    self.player.board.draw_pygame_board(self.player.board.field, self.player.ships, left_border_offset,
                                                        top_offset, False, screen)
                    self.player.board.draw_pygame_board(self.player.board.battlefield, self.comp.ships,
                                                        right_border_offset, top_offset, True, screen)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        elif event.type == pygame.MOUSEMOTION:
                            mouse_pos = pygame.mouse.get_pos()
                            highlight_coord = self.player.board.get_highlighted_cell_coordinate(mouse_pos)
                            if highlight_coord:
                                mouse_last_pos = highlight_coord
                        if event.type == pygame.MOUSEBUTTONDOWN and mouse_last_pos:
                            if self.chosen_coordinate_validation(mouse_last_pos, self.player, self.comp) is True:
                                if self.player.attack(mouse_last_pos, self.comp) is True:
                                    if self.ships_status_update(self.comp.ships) is False:
                                        winner = 'Player'
                                        running = False
                                        break
                                else:
                                    print('You missed')
                                    move = False
                            else:
                                print('You already hit that cell')

                    if mouse_last_pos:  # Highlight board cell
                        self.player.board.highlight_cell(mouse_last_pos, screen)

                    pygame.display.flip()
                    clock.tick(30)

                move = True
                while move and running:
                    if self.comp.attack(self.computer_choice(self.comp, self.player), self.player):
                        if self.ships_status_update(self.player.ships) is False:
                            winner = 'Computer'
                            running = False
                    else:
                        print('Computer missed')
                        move = False

            print(f'{winner}')

            pygame.quit()

game = Game()
game.start()