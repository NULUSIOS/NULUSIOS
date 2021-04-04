from art import logo
from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 100
EASY = 10
HARD = 5

not_found = True
hidden_number = randint(MIN_NUMBER, MAX_NUMBER)
last_min = MIN_NUMBER
last_max = MAX_NUMBER
difficulty = ""
play_again = True
guess = 0

while play_again == True:

  #intro
  print(logo)
  print(f"Welcome to guess the number.\nI already have a number in my mind, between {MIN_NUMBER} and {MAX_NUMBER}.")
  while difficulty != "easy" and difficulty != "hard":
    difficulty = input(f"Please enter 'easy' if you want to have {EASY} attempts\nor 'hard' if you want to have {HARD} attempts: ").lower()
  if difficulty == "easy":
    attempts = EASY
  else:
    attempts = HARD
  difficulty = ""

  #ask number loop
  while not_found and attempts != 0:
    #ask number
    print(f"\nRemaining attempts are {attempts}.")
    while guess > last_max or guess < last_min:
      guess = int(input(f"Give me a number betwen {last_min} and {last_max}: "))
    attempts -= 1
    if hidden_number < guess:
      last_max = guess - 1
      print("Number is lower.")
    elif hidden_number > guess:
      last_min = guess + 1
      print("Number is higher")
    else:
      not_found = False
      print("Your found it!")
    guess = 0
    if last_min == last_max:
      attempts -= 1
      not_found = False
      print(f"OK only one number remaining, so you found it with remaining {attempts} attempts.")

  if not_found:
    print("\nTough luck, better luck next time...")

  if input("To exit type 'x', else try another time: ").lower() == "x":
    play_again = False

