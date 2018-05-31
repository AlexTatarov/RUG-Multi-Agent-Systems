
from player import Player

class Computer(Player):
	def playCard(self, attacking_player, attacking_card=None):
		raise NotImplementedError
