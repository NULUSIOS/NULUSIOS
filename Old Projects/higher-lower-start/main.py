import random
from art import *
from game_data import data

lost = False
who = ""
score = 0

def format_nicely(selection):
  print(f"The item is: {selection['name']}.")
  print(f"It is: {selection['description']}.")
  print(f"Origin is: {selection['country']}.")

def check_won(chosen, a_side, b_side):
  if a_side["follower_count"] > b_side["follower_count"]:
    if chosen == a_side:
      return "yes"
    else:
      return "no"
  elif a_side["follower_count"] < b_side["follower_count"]:
    if chosen == b_side:
      return "yes"
    else:
      return "no"
  else:
    return "equal"

print(logo)

# select first random item
selection_a = random.choice(data)
data.remove(selection_a)


while not lost:
  # select second (new) random item
  selection_b = random.choice(data)
  data.remove(selection_b)

  #print properly
  print("A is:")
  format_nicely(selection_a)
  print(f"Follower count is: {selection_a['follower_count']}.")
  print(vs)
  print("B is:")
  format_nicely(selection_b)

  # ask which item followers are more
  while who != "a" and who != "b":
    who = input("\nSo who has more followers? (a or b) ").lower()
  if who == "a":
    select = selection_a
  else:
    select = selection_b
  who = ""
  # test win condition and if win add score and restart
  status = check_won(select, selection_a, selection_b)
  if status == "yes":
    print("You are right!")
    score += 1
  elif status == "no":
    print("Sorry, nope.")
    lost = True
  else:
    print("Weird but they have the same!")
    score += 1

  print(f"A has {selection_a['follower_count']} followers.")
  print(f"B has {selection_b['follower_count']} followers.")
  if data == []:
    print("You actually gone through the whole list! BRAVO!")
    lost = True

  # assign selection of B to A and prepare for new B
  selection_a = selection_b
  selection_b = []

# lost or list empty, show score
print(f"Your score is {score}")
