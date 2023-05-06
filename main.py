import player
import computer

comp = computer.Comp()
# player = computer.Comp()
player = player.Player()
player.ship_placement()

print(player.ships)
game = True
while True:
    while game:
        player.board.draw(player.ships, comp.ships)
        if player.attack(comp.ships, comp.board.field) is True:
            for ship in comp.ships:
                ship.status_update()
                if ship.status is True:
                    game = True
                    break
                else:
                    game = False
                    winner = 'Player'
        else:
            break
    while game:
        player.board.draw(player.ships, comp.ships)
        if comp.attack(player.ships, player.board.field) is True:
            for ship in player.ships:
                ship.status_update()
                if ship.status is True:
                    game = True
                    break
                else:
                    game = False
                    winner = 'Comp'
        else:
            break
    if game is False:
        player.board.draw(player.ships, comp.ships)
        print(f'{winner} wins!')
        break
