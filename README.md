

## Introduction

Durak is a card game that is popular in post-Soviet states. The objective of the game is to get rid of all one's cards when there are no more cards left in the deck. At the end of the game, the last player with cards in their hand is the *fool*.

## Task Description

## Progress

We've built a basic implementation of the game. 

### Card

The Card class is used to represent the cards present in a game of Durak. When a game starts one instance of the Card class is instantiated for each of the 36 cards. There are 4 suits: hearts, diamonds, clubs and spades and 9 different values for each suit from 6 to Ace.

### Game

The Game class runs the game of Durak. It knows about the players, all the cards, the deck, the discard pile and the common knowledge between the players. It takes care of attack cycles, turn taking, updating common knowledge and checking win conditions.

### Player

The Player class implements all the logic for a player in the game of Durak, including decision making. It knows which game it is playing, which hand it has and has knowledge of where all the cards in the game are. This knowledge is represented as a hashmap where the keys are instances of the Card class and the values are lists of places the card can be. (in the player's own hand, another player's hand, the deck or the discard pile)

### Computer

Computer is an extension of the Player class in which the game logic for the AI is implemented. The relevant method here is playCard(), which allows the player to choose a card from their hand that it wants to play. The method is invoked by Game and returns a Card object.

### User

User is an extension of the Player class and implements the decision making for the human player in the game. The simple implementation shows the user their hand and allows them to pick a card using a command prompt when it is the user's turn. If we build a GUI for the game, we should be able to easily hook this class up to click events in the user interface.

## Future Improvements
Build a UI for better representation of the game as stated above. Extend the game to more or less players (2-6), however it is not exactly the goal of this course. Implement different types of player behaviour for AI players. For example: 'aggressive' player (who would attack and risk more), 'cautious' player(who would attack and risk less and defend more), 'moderate' player (medium levels of aggresiveness and cautiousness). Try AI players determine the type of player they play against using knowledge database and change its own tactics based on that (needs the previous point with 'types of players' to be implemented).  



## About the Project:

This game is part of the final Project for the course [Multi-Agent Systems](https://www.rug.nl/ocasys/rug/vak/show?code=KIM.MAS03) at the [University of Groningen](https://www.rug.nl/). This project is developed by a team of three members:

1. Alex Tatarov (s3401332)
2. Micha de Rijk (s2671492)
3. Md. Ataur Rahman (s3521346)
