
import random

class Player:
	def __init__(self):
		self.game = None
		self.hand = set()
		self.knowledge = {}
	
	def joinGame(self, game):
		self.game = game
		self.hand = set() # reset hand
		
		# make general assumptions about the game
		self.knowledge = {}
		for card in self.game.cards: # each card can be either in the deck or in one of the player's hands
			self.knowledge[card] = set('deck')
			for i in range(len(self.game.players)):
				self.knowledge[card].add('player' + str(i))
		self.knowledge[self.game.trump_card] = ['deck'] # the trump card is in the deck
	
	def takeCard(self, card):
		self.hand.add(card)
		self.knowledge[card] = ['player1'] # the card is in our hand (TODO: figure out whether we are player 1, 2 or 3)
	
	def playCard(self, attacking_player, attacking_card=None):
		if attacking_card is None: # we are attacking
			card = random.choice(self.hand)
		else : # we are defending
			card = random.choice(self.hand)
		self.hand.remove(card) # delete the card from our hand
		return card

	def hasCard(self, suit, value):
		for h_card in self.hand:
			if h_card.eq(suit, value):
				return True

		return None 
