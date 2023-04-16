import player
import computer

comp = computer.Comp()
player = player.Player()

for x in range(100):
    comp.attack(player.ships, player.board.field)

comp.board.draw(comp.ships, player.ships)
player.board.draw(player.ships, comp.ships)


