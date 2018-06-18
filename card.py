

class Card:
	values = { # {<symbol>: <value>}
		'6': 0,
		'7': 1,
		'8': 2,
		'9': 3,
		'10': 4,
		'J': 5,
		'Q': 6,
		'K': 7,
		'A': 8,
	}
	suits = ('clubs', 'spades', 'hearts', 'diamonds')
	
	def __init__(self, value, suit, is_trump):
		self.value = value
		self.suit = suit
		self.is_trump = is_trump
	
	def __gt__(self, other):
		"""
		Allows greater than (>) checking between two Card objects.
		For example: Card('K', 'hearts', False) > Card('J', 'hearts', False)
		"""
		return self.suit == other.suit and ((self.is_trump == other.is_trump and self.values[self.value] > other.values[other.value]) or self.is_trump)
	
	def __lt__(self, other):
		"""
		Allows less than (<) checking between two Card objects.
		For example: Card('A', 'hearts', False) < Card('7', 'spades', True)
		"""
		return not (self > other)

	
	def __repr__(self):
		return '{}(value={}, suit={}, is_trump={})'.format(self.__class__, self.value, self.suit, self.is_trump)
