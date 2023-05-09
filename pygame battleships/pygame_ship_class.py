class Ship:
    def __init__(self, decks):
        self.decks = decks
        self.coordinates = {}
        self.orientation = int()
        self.status = True

    def status_update(self):
        if 1 not in self.coordinates.values():
            self.status = False
