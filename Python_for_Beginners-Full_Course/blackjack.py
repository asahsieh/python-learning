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
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
 
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
card = deal()
print(card)
cards_dealt = deal_ref(2)
print(cards_dealt)

# Let's seperate out the rank part of a single card
card = cards_dealt[0]
rank = card[1]
# print(rank)

## Each rank has a different value in blackjack, we need to set value to rank
### "A" is 11 or 1, we'll get to the one part later
### "J", "Q", "K" is 10
### the numbers have the value of the number
###
### This is the perfect time for a `conditional statement`

# Remember to use two equal signs instead fo one equal sign here 
if rank == "A":
    value = 11
elif rank == "J" or rank == "Q" or rank == "K":
    value = 10
else:
    value = rank 

# When that multiple values in a print statement are listed with a comma separating them, both values are printed with a space in between
print(rank, value)

# Use a `dictionary` to be more general, you can think of a dictionary as a mapping between a set of indices which are called keys and values
print("\n***** A dictionary for pairing rank and value *****")

rank_dict = {"rank": rank, "value": value}

print(rank_dict["rank"], rank_dict["value"])

# Refactor the code to get the value of each rank without using an if statement