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
    def deal(self, number):
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

deck1 = Deck()
deck2 = Deck()
deck2.shuffle()

# not shuffled
print("***** Deck without shuffled *****")
print(deck1.cards[0])

print(deck2.cards)

# Let's add safeguards to prevent errors every time the `deal` function is called, a card is removed from the cards list.
 
card = deck2.deal(1)
print(f"\ndealt card: {card}\n")

print("***** Test object of class Card *****")
card1 = Card("heart", {"rank": "K", "value": 10})
print(card1)