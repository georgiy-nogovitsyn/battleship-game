import pygame
import assets
from pygame_config import CELL
class Ship:
    def __init__(self, decks):
        self.decks = decks
        self.coordinates = {}
        self.orientation = int()
        self.status = True
        self.sprite = pygame.image.load(f'./assets/ship_{self.decks}.png')

    def status_update(self):
        if 1 not in self.coordinates.values():
            self.status = False

abc = Ship(4)

print(abc.sprite)
