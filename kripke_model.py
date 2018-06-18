

# Kripke model for one card

class KripkeModel:
	def __init__(self, states, relations):
		self.states = states # {<player>: <world_number>}
		self.relations = relations # {<player>: set((<world_number>, <world_number>))}
	
	def removePossibleWorld(self, player):
		""" Remove the state that represents a world in which <player> is holding the card. """
		state = self.states.get(player)
		if state is not None:
			for player, relations in self.relations.items():
				for relation in relations:
					if relation[0] == state or relation[1] == state:
						relations.remove(state)
			
			del self.states[player]
	
	def removeAllPossibleWorlds(self):
		""" Removes all states and relations in the Kripke model, because none of the players have the card in hand and everybody knows this. """
		self.states = {}
		for player in self.relations:
			self.relations[player] = {}
	
	def playerHasCard(self, player):
		""" Removes states and relations in the Kripke model in such a way that only the world in which <player> has the card is still considered a possible world. """
		for player2, world in self.states:
			if player2 != player:
				self.removePossibleWorld(player2)

