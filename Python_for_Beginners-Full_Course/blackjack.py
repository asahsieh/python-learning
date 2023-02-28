"""
Blackjack Card Game Project

To learn the techniques
- object-oriented programming in python

References
- https://www.hopenglish.com/a-deck-of-cards
"""

suits = ["spades", "hearts", "diamonds", "clubs"] 
suit = suits[2]
rank = "K"
value = 10
print("your card is: " + rank + " of " + suit)

# Add another item to the suits list
suits.append("snakes")

for suit in suits:
    print(suit) 