"""
Blackjack Card Game Project

To learn the techniques
- object-oriented programming in python

References
- https://www.hopenglish.com/a-deck-of-cards
"""

import random

cards = [] 
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
   # # a list with suit and ranks
   # print([suit, ranks[0]]) 

    # let's print every rank in every suit
    for rank in ranks:
       # print(suit + " " + rank)
       print([suit, rank])

       # let's append those 52 cards to the cards list
       cards.append([suit, rank])

print()
# All the cards are inorder in the cards lists 
#print(cards)

# To shuffled the cards by the `random` module
## random.shuffle(x): Shuffle the sequence x in place.
##
### To shuffle an immutable sequence and return a new shuffled list, use sample(x, k=len(x)) instead.

## by a function 
def shuffle():
    random.shuffle(cards)

# Move to after the deal() function 
# shuffle()
# print(cards)
# print()

# Let's remove a single element from the cards, this is similar to dealing a card from a deck by the `pop` method

## By a function also 
def deal():
    card = cards.pop()
    return card

## If you want the deal function to deal more than one card, to refactor the deal function  
def deal_ref(number):
    cards_dealt = []
    # use a the range function with a for loop
    for n in range(number):
        cards_dealt.append(cards.pop())
    return cards_dealt

shuffle()

# Refactor the code to get the value of each rank without using an if statement
## A new variable called `card` and assign to the card variable a single card that will deal from the deck but we'll make sure that card is not in a list 
## Change 

# A little tricky that dealing one card but to get the first item, it's going to the only item in the list 
card = deal_ref(1)[0]
print(card)

# to print value only
print(f"value: {card[1]['value']}")