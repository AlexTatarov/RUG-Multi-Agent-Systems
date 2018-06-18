
from card import Card
from computer import Computer
import random
import numpy as np

class Game:
	def __init__(self, players):
		self.cards = set()
		self.deck = []
		self.attacking_cards = []
		self.defending_cards = []
		self.discard_pile = []
		self.outcome = 0
		
		# smallest card that every player could not defend
		self.smallest = [[8] * 4 for y in range(len(players))]

		self.players = players
		self.common_knowledge = {}
		self.attacker = players[0]
		self.defender = players[1]
	
	def start(self):
		""" Initialize the deck and deal the starting hands. """
		trump_value = random.choice(list(Card.values))
		trump_suit = random.choice(Card.suits)
		self.trump_card = Card(trump_value, trump_suit, True)
		
		for value in Card.values:
			for suit in Card.suits:
				if suit == trump_suit and suit == trump_value: # skip trump card, we will add it later
					continue
				is_trump = (suit == trump_suit)
				card = Card(value, suit, is_trump)
				self.cards.add(card)
				self.deck.append(card)
		
		# shuffle the deck
		random.shuffle(self.deck)
		
		# add the trump card to the bottom of the deck
		self.deck.insert(0, self.trump_card)
		
		# deal cards
		for player in self.players:
			player.joinGame(self)
			for i in range(6):
				card = self.deck.pop() # take the top card from the deck
				player.takeCard(card) # add it to the players hand
		
		# initialize common knowledge
		for card in self.cards:
			self.common_knowledge[card] = ['deck'] + ['player' + str(i) for i in range(len(self.players))] # each card can be either in the deck or in one of the player's hands
		self.common_knowledge[self.trump_card] = ['deck'] # the trump card is in the deck
	
	def stop(self):
		""" Resets the game. """
		self.cards = set()
		self.deck = []
		self.attacking_cards = []
		self.defending_cards = []
		self.discard_pile = []
		self.common_knowledge = {}

		for player in self.players:
			player.hand = []

	def next_player(self, player):
		""" Return next player that has cards """
		for i in range(len(self.players)):
			if player == self.players[i]:

				if len(self.players[(i+1) % 4].hand) > 0:
					return self.players[(i+1) % 4]

				elif len(self.players[(i+2) % 4].hand) > 0:
					return self.players[(i+2) % 4]

				else:
					return self.players[(i+3) % 4]


	def next_turn(self, outcome):

		# player defended succesfully, so
		# defender becomes new attacker
		if outcome == 0:
			self.attacker = self.defender

			self.defender = self.next_player(self.attacker)

		# player failed to defend, so
		# defender skips turn to attack
		else:
			self.attacker = self.next_player(self.defender)

			self.defender = self.next_player(self.attacker)

	def new_attack(self):

		out = False

		while not out:
			
			card = self.attacker.playCard(self.attacker, self.defender)
			
			print('attacking card chosen ...')
			if card == None:
				return 0

			self.attacker.hand.remove(card)

			
			card = self.defender.playCard(self.attacker, self.defender)
			print('defending card chosen ...')
			if card == None:
				out = True
			else:
				self.defender.hand.remove(card)
		return 1

	def has_ended(self):

		counter = 0

		for player in self.players:
			if len(player.hand) > 0 :
				counter += 1

		if counter > 1:
			return False
		else:
			return True

def main():
	player_count = 4
	
	# create players
	players = []
	for i in range(player_count):
		player = Computer()
		players.append(player)
	
	# create a new game and let the players take actions until the game has ended
	game = Game(players)
	game.start()

	while not game.has_ended():

		print('New attack ...')
		outcome = game.new_attack()

		print('End of turn')
		game.next_turn(outcome)

if __name__ == '__main__':
	main()
