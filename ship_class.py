class Ship:
    def __init__(self, decks):
        self.decks = decks
        self.coordinates = {}
        self.orientation = int()
        self.status = True

    def status_update(self):
        lives = 0
        for x in self.coordinates.values():
            lives += x
        if lives <= 0:
            self.status = False
