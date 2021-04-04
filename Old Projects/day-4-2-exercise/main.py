# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

if len(names) < 2:
  print("Well you know who will pay the meal!")
else:
  who = names[random.randint(0,len(names)-1)]
 # print(f"{who} will pay the meal today!")
  print(random.choice(names) + " will pay the meal today!")

