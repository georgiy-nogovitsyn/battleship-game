import pygame
import pygame_player
from pygame_utils import highlight_cell, get_highlighted_cell_coordinate, draw_basic_board, draw_ships, draw_water_hits, \
    draw_board_numbers
from pygame_config import *
from pygame_main import Game
from random import choice

pygame.init()
clock = pygame.time.Clock()

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battleship Game Board")

arial_font = pygame.font.SysFont('arial', CELL)


def draw_pygame_elements():
    draw_basic_board(screen)
    draw_water_hits(screen, player.board.field)
    draw_water_hits(screen, comp.board.field, offset_x=right_border_offset)
    draw_ships(screen, player.ships)
    draw_ships(screen, comp.ships, hidden=True)
    draw_board_numbers(screen, arial_font)


events = Game()
player = pygame_player.Player(False)
comp = pygame_player.Player()

mouse_last_pos = []

player_1_turn = True
player_2_turn = False

final_message = 'Bye!'
running = True
while running:
    player_1_turn = True
    while player_1_turn:
        screen.fill(WHITE)

        draw_pygame_elements()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                player_1_turn = False

            elif event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                highlight_coord = get_highlighted_cell_coordinate(mouse_pos)
                if highlight_coord:
                    mouse_last_pos = highlight_coord

            if event.type == pygame.MOUSEBUTTONDOWN and mouse_last_pos:
                # Game events

                if events.chosen_coordinate_validation(mouse_last_pos, player, comp) is True:
                    if player.attack(mouse_last_pos, comp) is True:
                        print(f'You hit the ship on {mouse_last_pos}')
                        if events.ships_status_update(comp.ships) is False:
                            final_message = 'Player win!'
                            running = False
                            break
                    else:
                        print(f'You missed on {mouse_last_pos}')
                        player_1_turn = False
                else:
                    print(f'You already hit that {mouse_last_pos} cell')


        if mouse_last_pos:
            highlight_cell(screen, mouse_last_pos)

        pygame.display.flip()
        clock.tick(30)
    player_2_turn = True
    while player_2_turn:
        if coordinates_for_attack := events.searching_for_destroy(comp, player):
            computer_choice_coordinates = choice(coordinates_for_attack)
        else:
            computer_choice_coordinates = events.computer_choice(comp, player)
        if comp.attack(computer_choice_coordinates, player):
            print(f'Computer hit the ship on {computer_choice_coordinates}')
            if events.ships_status_update(player.ships) is False:
                final_message = 'Computer Win!'
                running = False
                break
        else:
            print(f'Computer missed on {computer_choice_coordinates}')
            player_2_turn = False

print(final_message)
pygame.quit()
