from src.core.player import Player
from src.core.game import Game

player_names = ['Ronnie', 'Dana', 'Adir', 'Itamar', 'Liad']

players = [Player(p_name) for p_name in player_names]

game = Game(players=players)

game.start()

