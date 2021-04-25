#!/usr/bin/env python3

import random

#App bootup screen in the command prompt. 
def Welcome():
  print("Welcome to Guess My Number!")
  print("""
  Enter 'Play' to play the game.
  Enter 'Menu' to come back to the menu.
  Enter 'Exit' to quit the game.
  """)

#Activated by the Play selection from the startup menu.
def Start_Game():
  attempt = 0
  High_Score = ""
  High_Score_Player = ""
  number = random.randint(1, 100)
  player = input("What is your name?")
  print("Welcome {}, to Guess My Number!".format(player))
  Guess_My_Number(attempt, High_Score, High_Score_Player, number, player)

#Activated once the user guesses the correct number.   
def Play_Again(attempt, High_Score, High_Score_Player, player):
  player = player
  play_again = input("Would you like to play again? (Y/N) ")
  if play_again.title().startswith("Y"):
    New_Game(attempt, High_Score, High_Score_Player, player)      
  else:
    print("Thanks for playing!")
    print("""
    Please type 'Exit' to leave the game 
    or type 'Menu' to return to the menu.
    """)

#Activated if the user enters "Y" when prompted to play again.    
def New_Game(attempt, High_Score, High_Score_Player, player):
  
  number = random.randint(1, 100)
  player = input("What is your name?")
  attempt = 0
  Guess_My_Number(attempt, High_Score, High_Score_Player, number, player)

#Guess input loop to handle errors caused by the user input for the guess variable.
def getGuess():
  while True:
    try:
      guess = int(input("What do you think my number is? "))
      return guess
    except ValueError as err:
      print("The value you entered is not an integer. Please try again.")
      
def Guess_My_Number(attempt, High_Score, High_Score_Player, number, player):
  if High_Score != "":
    print("""
    High Score
    {}    {}
    """.format(High_Score_Player, High_Score))
  else:
    print("The number will be between 1 and 100.")

  #Guess loop that provides responses based on the user's input.
  guess = -1
  while guess != number:
    guess = getGuess()
    if guess > 100:
      print("The number is below 100.")
      continue
    elif guess < 1:
      print("The number is higher than 0.")
      continue
    elif guess < number:
      print("The number is higher than {}.".format(guess))
      attempt += 1
      continue
    else:
      print("The number is lower than {}.".format(guess))
      attempt +=1
      continue

  #The player guessed the correct number and has their score evaluated against the current high score.
  if High_Score == "":
    High_Score = attempt
    High_Score_Player = player
  elif attempt < High_Score:
    High_Score = attempt
    High_Score_Player = player
  else:
    High_Score = High_Score

  plural = "s" if attempt != 1 else ""
  print("Congratulations {}! You guessed the number in {} attempt{}.".format(player, attempt, plural))

  Play_Again(attempt, High_Score, High_Score_Player, player)

#Initiates the player menu.   
Welcome()
while True:
  new_selection = input("> ")
  new_selection = new_selection.title()
  if new_selection == 'Exit':
    break
  elif new_selection =='Menu':
    Welcome()
    continue
  elif new_selection =='Play':
    Start_Game()
    continue


