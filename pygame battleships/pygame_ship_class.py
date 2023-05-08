class Ship:
    def __init__(self, decks):
        self.decks = decks
        self.coordinates = {}
        self.orientation = int()
        self.status = self.status_update()

    def status_update(self):
        lives = 0
        for x in self.coordinates.values():
            lives += x
        if lives <= 0:
            print('Ship is dead')
            return False
        else:
            return True
