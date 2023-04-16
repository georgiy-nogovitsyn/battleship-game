class Ship:
    def __init__(self, decks):
        self.decks = decks
        self.coordinates = {}

    def status_update(self):
        lives = 0
        for x in self.coordinates.values():
            lives += x
        return lives
