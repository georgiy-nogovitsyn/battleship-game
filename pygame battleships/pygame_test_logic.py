import pygame
from pygame_player import Player
from pygame_utils import highlight_cell, get_highlighted_cell_coordinate, draw_basic_board, draw_ships, draw_water_hits, \
    draw_board_numbers, draw_pygame_message
from pygame_config import *
from pygame_main import Game
from random import choice
from time import time

pygame.init()
clock = pygame.time.Clock()

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battleship Game Board")

# Set pygame font
arial_font = pygame.font.SysFont('arial', CELL)

message = ''
def draw_pygame_elements():
    draw_basic_board(screen)
    draw_water_hits(screen, player.board.field)
    draw_water_hits(screen, comp.board.field, offset_x=right_border_offset)
    draw_ships(screen, player.ships)
    draw_ships(screen, comp.ships, hidden=True)
    draw_board_numbers(screen, arial_font)
    draw_board_numbers(screen, arial_font, offset=right_border_offset)
    draw_pygame_message(screen, arial_font, message)


# Creating class objects
events = Game()
player = Player(False)
comp = Player()

mouse_last_pos = []

player_1_turn = True
player_2_turn = False

# initialize millis counters
millis = time() * 1000.0
saved_millis = millis

final_message = 'Bye!'
running = True
for x in comp.ships:
    print(x.coordinates)
while running:
    screen.fill(WHITE)
    draw_pygame_elements()

    if mouse_last_pos:
        highlight_cell(screen, mouse_last_pos)

    clock.tick(30)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            player_1_turn = False


        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            highlight_coord = get_highlighted_cell_coordinate(mouse_pos)
            if highlight_coord:
                mouse_last_pos = highlight_coord

        if player_1_turn:
            if event.type == pygame.MOUSEBUTTONDOWN and mouse_last_pos:
                # Game events
                if events.chosen_coordinate_validation(mouse_last_pos, player, comp) is True:
                    if player.attack(mouse_last_pos, comp) is True:
                        message = f'You hit the ship in {mouse_last_pos}'
                        print(f'You hit the ship on {mouse_last_pos}')
                        if events.ships_status_update(comp.ships) is False:
                            final_message = 'Player win!'
                            running = False
                            break
                    else:
                        message = f'You missed on {mouse_last_pos}'
                        print(f'You missed on {mouse_last_pos}')
                        player_2_turn = True
                        player_1_turn = False
                else:
                    message = f'You already hit that {mouse_last_pos} cell'
                    print(f'You already hit that {mouse_last_pos} cell')

    millis = time() * 1000.0  # update millis

    if player_2_turn and millis - saved_millis >= 0:
        if coordinates_for_attack := events.searching_for_destroy(comp, player):
            computer_choice_coordinates = choice(coordinates_for_attack)
        else:
            computer_choice_coordinates = events.computer_choice(comp, player)
        if comp.attack(computer_choice_coordinates, player):
            message = f'Computer hit the ship on {computer_choice_coordinates}'
            print(f'Computer hit the ship on {computer_choice_coordinates}')
            if events.ships_status_update(player.ships) is False:
                final_message = 'Computer Win!'
                running = False
                break
        else:
            message = f'Computer missed on {computer_choice_coordinates}'
            print(f'Computer missed on {computer_choice_coordinates}')

            player_1_turn = True
            player_2_turn = False

        # saving millis to delay comp move
        saved_millis = time() * 1000.0 + 1500

print(final_message)
pygame.quit()
