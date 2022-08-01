from src.core.player import Player

class Game:
    def __init__(self, players: list[Player]):
        self.players = players

    def announce_turn(self, player: Player):
        print(f"It is {player.name}'s turn:")

    def start(self):
        while True:
            for player in self.players:
                self.announce_turn(player)

