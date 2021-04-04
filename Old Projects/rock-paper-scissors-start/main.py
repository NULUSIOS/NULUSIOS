rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

user_selection = int(input("What's your choice? (0 Rock, 1 Paper, 2 Scissors) "))

hand = [rock,paper,scissors]
comp_selection = random.randint(0,2)

if user_selection == comp_selection:
  print(f"\n{hand[user_selection]}\n\nComputer chose:\n{hand[comp_selection]}\n\n")
  print("It's a tie.")
elif (user_selection - comp_selection == 1) or (comp_selection - user_selection == 2):
  print(f"\n{hand[user_selection]}\n\nComputer chose:\n{hand[comp_selection]}\n\n")
  print("You win!")
elif (user_selection - comp_selection == -1) or (comp_selection - user_selection == -2):
  print(f"\n{hand[user_selection]}\n\nComputer chose:\n{hand[comp_selection]}\n\n")
  print("You lose!")
else:
  print("You did something stupid, so you lose!")
