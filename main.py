import player
import computer

comp = computer.Comp()
player = player.Player()
player.ship_placement()

for x in range(100):
    comp.attack(player.ships, player.board.field)
    print(x)

for ship in player.ships:
    print(ship.status_update())
comp.board.draw(comp.ships, player.ships)
player.board.draw(player.ships, comp.ships)


