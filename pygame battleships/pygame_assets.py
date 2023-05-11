import pygame
from pygame_config import CELL

ship_sprite_1 = pygame.image.load('assets/ship_1.png')
ship_sprite_2 = pygame.image.load('assets/ship_2.png')
ship_sprite_3 = pygame.image.load('assets/ship_3.png')
ship_sprite_4 = pygame.image.load('assets/ship_4.png')

ship_1 = pygame.transform.scale(ship_sprite_1,(CELL, CELL))
ship_2 = pygame.transform.scale(ship_sprite_2,(CELL * 2, CELL))
ship_3 = pygame.transform.scale(ship_sprite_3,(CELL * 3, CELL))
ship_4 = pygame.transform.scale(ship_sprite_5,(CELL * 4, CELL))

ship_hit = pygame.image.load('assets/ship_shot.png')
water_hit = pygame.image.load('assets/water_shot.png')