
from player import Player

class User(Player):
	def playCard(self, attacking_player, attacking_card=None):
		raise NotImplementedError
