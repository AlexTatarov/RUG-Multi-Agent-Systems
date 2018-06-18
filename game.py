
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
			for i in range(int(36/len(self.players))):
				card = self.deck.pop() # take the top card from the deck
				player.takeCard(card) # add it to the players hand
		
		# initialize common knowledge
		for card in self.cards:
			self.common_knowledge[card] = ['player' + str(i) for i in range(len(self.players))] # each card can be either in the deck or in one of the player's hands



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

	def suit_to_nr(self, suit):
		if suit == 'clubs':
			return 0
		elif suit == 'diamonds':
			return 1
		elif suit == 'hearts':
			return 2
		else:
			return 3

	def player_to_string(self, player):

		if player == self.players[0]:
			return 'player1'

		elif player == self.players[1]:
			return 'player2'
		
		elif player == self.players[2]:
			return 'player3'
		
		else:
			return 'player4'

	def player_to_nr(self, player):

		if player == self.players[0]:
			return 0

		elif player == self.players[1]:
			return 1
		
		elif player == self.players[2]:
			return 2
		
		else:
			return 3


	def next_turn(self, outcome):

		# player defended succesfully, so
		# defender becomes new attacker
		if outcome == 0:
			# transfer cards to discard pile
			for card in self.attacking_cards:
				self.discard_pile.append(card)
				self.updateKnowledge(card, 'discard_pile')

			for card in self.defending_cards:
				self.discard_pile.append(card)
				self.updateKnowledge(card, 'discard_pile')

			# reset cards on table
			self.attacking_cards = []
			self.defending_cards = []

			# change attacker and defender
			self.attacker = self.defender
			self.defender = self.next_player(self.attacker)

		# player failed to defend, so
		# defender skips turn to attack
		else:

			# transfer cards from table to defender's hand
			for card in self.attacking_cards:
				self.defender.hand.add(card)
				self.updateKnowledge(card, self.defender)

			for card in self.defending_cards:
				self.defender.hand.add(card)
				self.updateKnowledge(card, self.defender)

			attacking_suits = [0, 0, 0, 0]
			for x in range(len(self.defending_cards)):
				def_card = self.defending_cards[x]
				att_card = self.attacking_cards[x]

				if def_card.suit != att_card.suit and attacking_suits[self.suit_to_nr(att_card)] == 0:
					self.smallest[self.suit_to_nr(att_card.suit)][self.player_to_nr(self.defender)] = att_card.value

				attacking_suits[self.suit_to_nr(att_card.suit)] += 1

			if len(self.defending_cards) == 0:
				self.smallest[self.suit_to_nr(self.attacking_cards[0])][self.player_to_nr(self.defender)] = self.attacking_cards[0].value
				attacking_suits[self.suit_to_nr(self.attacking_cards[0])] = 1

			for x in range(4):
				if attacking_suits[x] > 0:
					self.smallest[x][self.player_to_nr(self.defender)] = 8

			# reset cards on table
			self.attacking_cards = []
			self.defending_cards = []

			# change attacker and defender
			self.attacker = self.next_player(self.defender)
			self.defender = self.next_player(self.attacker)

	def updateKnowledge(self, card, location):

		for player in self.players:
			player.knowledge[card] = [self.player_to_string(location)]

	def new_attack(self):

		print(self.player_to_string(self.attacker) + ' attacks')
		print(self.player_to_string(self.defender) + ' defends')
		
		out = False

		while not out:
			
			card = self.attacker.playCard(self.attacker, self.defender)
			

			if card == None:
				return 0
			print('Attacking card chosen:')
			print(card.suit)
			print(card.value)
			print(str(card.is_trump))
			print()
			self.updateKnowledge(card, 'table')

			self.attacking_cards.append(card)

			self.attacker.hand.remove(card)

			
			card = self.defender.playCard(self.attacker, self.defender, card)
			if card == None:
				print('Defender can not defend')
				print()
				out = True
			else:
				print('Defending card chosen:')
				print(card.suit)
				print(card.value)
				print(str(card.is_trump))
				print()
				self.updateKnowledge(card,'table')

				self.defending_cards.append(card)
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
