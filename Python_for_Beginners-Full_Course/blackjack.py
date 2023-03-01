"""
Blackjack Card Game Project

To learn the techniques
- object-oriented programming in python

References
- https://www.hopenglish.com/a-deck-of-cards
"""

import random

# Card class 
class Card:
    # Set self.suit to equal hearts
    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank 

    # It's called when print is invoked on an object from the calss 
    ## return a string
    ### We want to make it so when we print an object from the card class, it will print something like 10 of hearts, or 3 of clubs, etc.  
    def __str__(self) -> str:
        #return self.rank["rank"] + " of " + self.suit
        # by f-string to put the variables right within the string
        return f"{self.rank['rank']} of {self.suit}"

# Define classes that will be used in order to separate out different aspects of the game
## Classes provide a way of bundling data and functionality together
## We're going to use classes to model three parts of the game 
### A card, a deck, and a hand

class Deck:
    # always have to pass in `self` to all of these functions in a class because then it gets itself is referring to the instance of the class 
    # Anything inside the parentheses remember is called an argument
    def __init__(self):
        self.cards = [] 
        suits = ["spades", "hearts", "diamonds", "clubs"] 
        ranks = [
                {"rank": "A", "value": 11},
                {"rank": "2", "value": 2},
                {"rank": "3", "value": 3},
                {"rank": "4", "value": 4},
                {"rank": "5", "value": 5},
                {"rank": "6", "value": 6},
                {"rank": "7", "value": 7},
                {"rank": "8", "value": 8},
                {"rank": "9", "value": 9},
                {"rank": "10", "value": 10},
                {"rank": "J", "value": 10},
                {"rank": "Q", "value": 10},
                {"rank": "K", "value": 10}
            ]
    
        # cards should be suits x ranks, total of 52 items or cards
        for suit in suits:
            for rank in ranks:
                # Create and append an instance of the card class and
                # afterwards when a deck is created, it's filled with cards
                self.cards.append(Card(suit, rank))
    
    # To shuffled the cards by the `random` module
    ## random.shuffle(x): Shuffle the sequence x in place.
    ##
    ### To shuffle an immutable sequence and return a new shuffled list, use sample(x, k=len(x)) instead.
    
    # Using the `self` keyword, the function can access the attributes and methods of the class  
    def shuffle(self):
        # A deck with only one card does not need to be shuffled
        if len(self.cards) > 1:
            random.shuffle(self.cards)
        else:
            print("Only one card, no need to do shuffle.")
   
    ## If you want the deal function to deal more than one card, to refactor the deal function  
    def deal(self, number=1):
        cards_dealt = []
        # For testing the safeguards on IndexError
        #self.cards = []

        # use a the range function with a for loop
        for x in range(number):
            # You can only remove a card if there are cards to remove.
            ## So, before the program tries to pop a card off self.cards, is to check if the length of self.cards is greater than zero
            ### Way 1:
            # try:
            #     self.cards.pop()
            # except IndexError:
            #     print("Oops!  cards is empty.")
            #     exit(1)
            # else:
            #   cards_dealt.append(self.cards.pop())

            ### Way 2 from the course:
            if len(self.cards) > 0:
                cards_dealt.append(self.cards.pop())
            else:
                print("Oops!  cards is empty.")
                exit(1)

        return cards_dealt

# Hand class
#
# In this blackjack game, there will be a human controlled player and a program controlled dealer
## So, let's add a dealer parameter in the init constructor method
## Dealer should be set to true or false to keep track of what type of hand it is 
# 
# Methods:
## calculate_value
### calculate the value of a hand
 
class Hand:
    def __init__(self, dealer=False) -> None:
        self.cards = []
        self.value = 0
        self.dealer = dealer 

    def add_card(self, card_list):
        self.cards.extend(card_list)
    
    def calculate_value(self):
        self.value = 0
        has_ace = False

        for card in self.cards:
            self.value += int(card.rank["value"])
            if card.rank["rank"] == "A":
                has_ace = True
        
        # After this entire for loop, We're going to check if the card has an ace and if the value is over 21, if so, then we'll just subtract 10 from the value, because that'll be the same as setting the ace to equal one instead of 11.
        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        # calculate the value before we return the value
        self.calculate_value()
        return self.value

    # Total value is 21 
    def is_blackjack(self) -> bool:
        # if self.get_value() == 21:
        #     print("You have a blackjack, congratulations!")
        #     return True
        # elif self.get_value() > 21:
        #     print("Oops! There's Bust.")
        #     return False 
        # else: 
        #     print("Great! The total value smaller than 21.")
        #     return False 
        return self.get_value() == 21 

    def display(self, show_all_dealer_cards=False):
        # Use three single quotes to use double qoutes and single quotes within this string
        print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')

        # The first card should display as hidden
        ## We're going to need to get access to the card index
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer \
            and not show_all_dealer_cards and not self.is_blackjack():
                print("hiddle")
            else:
                print(card)

        if not self.dealer:
            print("Value: ", self.get_value())
        print()

class Game:
    def play(self):
        game_number = 0
        games_to_play = 0

        # Set games_to_play to be whatever the user inputs after they're asked how many games do you want to play
        ## make sure the games to play is an `int`

        # There's a potential for an error on puting an character (e.g., 'u'):
        # ValueError: invalid literal for int() with base 10: 'u'
        ## Create a try-except block to handle the exception

        # Make the program keep asking the user for a value until the user enters a number

        while games_to_play <= 0:
            try: 
                games_to_play = int(input("How many games do you want to play? "))
            except:
                print("You must enter a number.")

        # Create number of games to play 
        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            # Add a card to the player's hand that is dealt from the deck and also a add card to the dealer's hand that is dealt from the deck also 

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            # Print an asterisk 30 time to make a divder
            # print("******************************")
            ## A trick to printing something a lot of times
            print("*" * 30)

            # Print the current game number out of the total number of games
            # like game 4 of 10
            print(f"Game {game_number} of {games_to_play}")

            print("*" * 30)
            player_hand.display()
            dealer_hand.display()
        
            # At this point in the game, someone could already have won if they got a blackjack
            if self.check_winner(player_hand, dealer_hand):
                # Go on the the next game if there is a winner
                continue

            # At this point in the game, the player will be able to choose hit or stand
            ## The player should be able to keep choosing until the value of their hand is over 21.
            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]: 
                choice = input("Please choose 'Hit' or 'Stand' (or H/S): ").lower()
                print()
                if choice in ["hit", "h"]:
                    player_hand.add_card(deck.deal())
                    player_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                # Go on the the next game if there is a winner
                continue

            # Store the value of player's hand in a variable 
            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            # Dealer should keep drawing card until dealer hand value is more than 17
            while dealer_hand_value <= 17:
                dealer_hand.add_card(deck.deal())
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_cards=True)

            if self.check_winner(player_hand, dealer_hand):
                # Go on the the next game if there is a winner
                continue

            # Print the final result
            print("Final Results")
            print("Your hand:", player_hand_value)
            print("Dealer's hand:", dealer_hand_value)

            # Call the check winner function one final time
            ## Pass in the hands like before but this is time we'll add a third argument of True to indicate that the game is over
            self.check_winner(player_hand, dealer_hand, True)
        
        print("\nThanks for playing!")

    def check_winner(self, player_hand, dealer_hand, game_over=False) -> bool:
        # the game can also end if both players choose not to get more cards. Use `game_over` to specifiy this
        if not game_over:
            # Check whether player's hand is greater than 21
            # If so, we'll print you busted dealer
            if player_hand.get_value() > 21:
                print("You busted. Dearler wins! 😭")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer busted. You wins! 😄")
                return True
            # check whether has blackjack
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack(): 
                print("Both players have blackjack! Tie! 😐")
                return True
            elif player_hand.is_blackjack():
                print("You have blackjack. You wins! 😄")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer have blackjack. Dearler wins! 😭")
                return True
        else: 
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win! 😄")
            elif dealer_hand.get_value() > player_hand.get_value():
                print("Dealer win! 😄")
            else:
                print("Tie! 😐")
            return True

        return False

g = Game()
g.play()

