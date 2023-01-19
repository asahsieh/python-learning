# Code of Rock Paper Scissors (RPS) game

# Libraries
import random

# Variables and Functions
def get_choices():
    # User Input
    player_choice = input("Enter a choice (rock, paper, scissors): ") 
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options) 
    # Dictionaries
    choices = {"player": player_choice, "computer": computer_choice}
    return choices 

# Function Arguments
def check_win(player, computer):
    # f-strings
    # print("You chose" + player + ", computer chose" + computer)
    print(f"You chose \"{player}\", Computer chose \"{computer}\"")
    if player == computer:
        # return [player, computer]
        return "It's a tie!"
    #elif player == "rock" and computer == "scissors":
    #    return "Rock smashes scissors! You win!"
    #elif player == "rock" and computer == "paper":
    #    return "Paper covers rock! You lose."

    # Refactoring and Nested If
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else: # computer == "paper"
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
          return "Paper covers rock! You win!"
        else:
          return "Scissors cuts paper! You lose."
    elif player == "scissors":
      if computer == "paper":
        return "Scissors cuts paper! You win!"
      else:
        return "Rock smashes scissors! You lose."

# If Statements 
#a = 3
#b = 5
#if a == b:
#    print("yes")

# def greeting():
#     return "Hi"

# Calling Functions
# response = greeting()
# print(f"{response}\n")

choices = get_choices()
print(f"\N{GREEK CAPITAL LETTER DELTA} Returned dictionary from get_choices(): {choices}\n")
# Accessing Dictionary Values
## quick example
#choices = {"player": "rock", "computer": "paper"}
#p_choice = choices["player"]
#c_choice = choices["computer"]

result = check_win(choices["player"], choices["computer"])
print(result)

# Lists, Methods
#food = ["pizza", "carrots", "eggs"]
#dinner = random.choice(food)
#print(f"Dinner is {dinner}.")