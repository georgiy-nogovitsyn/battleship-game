class Ship:
    def __init__(self, coords):
        self.coords = coords
        self.decks = len(coords)
        self.health = self.decks