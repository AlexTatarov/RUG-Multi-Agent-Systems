
from card import Card
from computer import Computer
from kripke_model import KripkeModel
import random

class Game:
	def __init__(self, players):
		self.cards = set()
		self.deck = []
		self.attacking_cards = []
		self.defending_cards = []
		self.discard_pile = []
		
		# smallest card that every player could not defend
		self.smallest = [[8 for x in range(4)] for y in range(players)]

		self.players = players
		self.kripke_model = {} # {<card>: KripkeModel(states={<player>: <world_number>}, relations={<player>: set((<world_number>, <world_number>))})}
	
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
		for index, player in enumerate(self.players):
			player.joinGame(self)
			for i in range(6):
				card = self.deck.pop() # take the top card from the deck
				player.takeCard(card) # add it to the players hand
		
		# initialize common knowledge
		for card in self.cards:
			states = {player: index for player, index in enumerate(players)}
			relations = {
				player: set((i, j) for i in range(len(players)) for j in range(len(players)))
				for player in self.players
			}
			self.kripke_model[card] = KripkeModel(states, relations)
		
		# the trump card is not in any of the player's hands and they all know it
		for player in self.players:
			self.kripke_model[self.trump_card] = None
	
	def stop(self):
		""" Resets the game. """
		self.cards = set()
		self.deck = []
		self.attacking_cards = []
		self.defending_cards = []
		self.discard_pile = []
		self.kripke_model = {}
		
		for player in self.players:
			player.hand = []
	
	def next_action(self):
		""" Simulate the next action. """
		self.has_ended = True

def main():
	player_count = 3
	
	# create players
	players = []
	for i in range(player_count):
		player = Computer()
		players.append(player)
	
	# create a new game and let the players take actions until the game has ended
	game = Game(players)
	game.start()
#	while not game.has_ended:
#		game.next_action()

if __name__ == '__main__':
	main()
