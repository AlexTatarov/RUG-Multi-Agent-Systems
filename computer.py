
from player import Player
from game import Game
import random
class Computer(Player):

	def checkValue(self, attacking_player, card_value):

		# find all cards with certain value
		for card in Game.cards
			if (card.value == card_value):
				# check if attacking player has this card
				for place in Game.common_knowledge[card]:
					if (place == attacking_player):
						return card

		return None

	def playCard(self, attacking_player, defending_player, attacking_card=None):

		if(defending_player == 'player1'):
			def_player = 0
		if(defending_player == 'player2'):
			def_player = 1
		if(defending_player == 'player3'):
			def_player = 2
		if(defending_player == 'player4'):
			def_player = 3

		### player DEFENDS
		if len(Game.attacking_cards) != len(Game.defending_cards):
			
			#possible_cards = []
			
			chosen_card = None

			for card in self.hand:
				if card.gt(attacking_card):
					if(chosen_card == None || chosen_card.gt(card)):
						chosen_card = card

			# if chosen_card == None then he can not defend this attack

			"""
			### choose randomly defending card
			chosen_card = random.choice(possible_cards)

			### choose best card using knowledge

			# cards with value that attacking player does not have
			unique_cards = []

			for card in possible_cards:
				same_value = checkValue(attacking_player, card.value)
				if(same_value != None):
					# attacking player has a card with this value
					used_attacking_cards = []
					used_attacking_cards.append(same_value)
					defensive_card = checkDefense(same_value)
					used_defending_cards = []

				else:
					# attacking player does not have a card with this value
					unique_cards.append(card)

			"""
			return chosen_card

		else:

			### PLAYE RINITIATES ATTACK
			if len(Game.attacking_cards) == 0 : 
				### player can choose any card to INITIATE ATTACK

				# choose card randomly
				#chosen_card = random.choice(self.hand)

				# check if you have only tramp cards or not
				simple = False

				for card in self.hand:
					if !card.is_trump:
						simple = True
						break

				if simple:
				# find suit with less cards 
					def_suit_nr = {}

					possible_cards = []

					for suit in Cards.suits:
						def_suit_nr[suit] = 0

					for card in Game.cards:
						for place in self.knowledge[card]:
							if place == defending_player:
								def_suit_nr[card.suit] += 1
								
					# if there is knowledge of some highest card for a suit use that knowledge
					# else use the suit with least cards
					for suit in range(0,4):
						if(Game.smallest[suit][def_player] < 8):
							for value in range(Game.smallest[suit][def_player], 8):
								card = self.hasCard(suit, value)
								if(card != None):
									possible_cards.append(card)

					# check if you have the last cards of some suit
					discarded_suit = {}
					own_suit = {}

					for suit in Card.suits:
						discard_suit[suit] = 0
						own_suit[suit] = 0

					for card in Game.discard_pile:
						discard_suit[card.suit] += 1

					for card in self.hand:
						own_suit[card.suit] += 1

					for suit in Card.suits:
						if (own_suit[suit] + discard_suit[suit] == 9):
							for card in self.hand:
								if card.suit == suit:
									possible_cards.append(card)

					# find suit with most cards
					most_suit = Card.suits[0]
					
					for suit in Card.suits:
						if own_suit[suit] > own_suit[most_suit]:
							most_suit = suit

					if len(possible_cards) > 0:

						chosen_card = possible_cards[0]						

						for card in possible_cards:
							if !card.is_trump:
								if card.lt(chosen_card) or (own_suit[chosen_card] > own_suit[card]):
									chosen_card = card
							else:
								if card.lt(chosen_card):
									chosen_card = card
					else:

						chosen_card = self.hand[0]

						for card in self.hand:
							if card.lt(chosen_card) or (own_suit[chosen_card] > own_suit[card]):
								chosen_card = card	
					
				# if we have only trump cards choose the smallest to attack
				else:
					chosen_card = self.hand[0]
					for card in self.hand:
						if chosen_card.gt(card):
							chosen_card = card

			# PLAYER CONTINUES ATTACK
			else:
				
				possible_cards = []

				played_cards = []

				# select all played cards
				for card in Game.attacking_cards:
					played_cards.append(card)

				for card in Game.defending_cards:
					played_cards.append(card)

				# choose cards that could be used
				for card in self.hand:
					for played in played_cards:
						if(played.value == card.value):
							possible_cards.append(card)

				chosen_card = None

				# if there are any possible cards to use
				if len(possible_cards) > 0:
					for card in possible_cards:
						if(Game.smallest[card.suit][def_player] <= card.value):
							chosen_card = card

					if(chosen_card == None):
						for card in possible_cards:
							if (chosen_card == None) || (own_suit[chosen_card.suit] > own_suit[card.suit]):
								chosen_card = card

				# otherwise no card can be played
				else:
					chosen_card = None
				
		return chosen_card
