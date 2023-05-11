import pygame_player
import pygame
from pygame_config import *

from random import randint, choice

pygame.init()
clock = pygame.time.Clock()

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battleship Game Board")


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
                return True
        return False

    def computer_choice(self, attacker, opponent):
        while True:
            choice = randint(0, 9), randint(0, 9)
            if self.chosen_coordinate_validation(choice, attacker, opponent):
                return choice

    def searching_for_destroy(self, attacker, opponent):
        coordinates_for_attack = []
        for ship in opponent.ships:
            if ship.status is True and 0 in ship.coordinates.values():
                for coordinate in ship.coordinates:
                    if ship.coordinates[coordinate] == 0:
                        for x in range(coordinate[0] - 1, coordinate[0] + 2):
                            for y in range(coordinate[1] - 1, coordinate[1] + 2):
                                if attacker.board.battlefield.get((x, y)) == 1 and ship.coordinates.get((x, y)) == 1:
                                    coordinates_for_attack.append((x, y))
        return coordinates_for_attack

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
                                    print(f'You hit the ship on {mouse_last_pos}')
                                    if self.ships_status_update(self.comp.ships) is False:
                                        winner = 'Player'
                                        running = False
                                        move = False
                                        break
                                else:
                                    print(f'You missed on {mouse_last_pos}')
                                    move = False
                            else:
                                print(f'You already hit that {mouse_last_pos} cell')

                    if mouse_last_pos:  # Highlight board cell
                        self.player.board.highlight_cell(mouse_last_pos, screen)

                    pygame.display.flip()
                    clock.tick(30)

                move = True
                while move and running:
                    if coordinates_for_attack := self.searching_for_destroy(self.comp, self.player):
                        computer_choice_coordinates = choice(coordinates_for_attack)
                    else:
                        computer_choice_coordinates = self.computer_choice(self.comp, self.player)
                    if self.comp.attack(computer_choice_coordinates, self.player):
                        print(f'Computer hit the ship on {computer_choice_coordinates}')
                        if self.ships_status_update(self.player.ships) is False:
                            winner = 'Computer'
                            running = False
                            break
                    else:
                        print(f'Computer missed on {computer_choice_coordinates}')
                        move = False

            print(f'{winner}')

            pygame.quit()

game = Game()
game.start()