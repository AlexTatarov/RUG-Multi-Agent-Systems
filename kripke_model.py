

# Kripke model for one card

class KripkeModel:
	def __init__(self, states, relations):
		self.states = states # {<player>: <world_number>}
		self.relations = relations # {<player>: set((<world_number>, <world_number>))}


