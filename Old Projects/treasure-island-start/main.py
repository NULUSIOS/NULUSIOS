print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print('''
You are in a path that splits to (L)eft and (R)ight.
To the left the path make a sharp turn and you cannot see beyond.
To the right you can reach a deserted harbor.
''')
direction = input("Where do you choose to go? ").lower()
if direction == "l": # and possibly handle other directions versions
  print("I am sorry... right after the sharp turn, you are too late to see a very deep hole.\nYou are dead.-")
elif direction == "r":
  print("You reached the harbor.\nThe water is very deep, but just 100 meters from the shore, there is a little island and you can see something glowing on its shore.\nYou see a ship coming to dock.")
  command = input("Will you (w)ait or you want to (s)wim to the island? ").lower()
  if command == "s":
    print("Well, the water was deep enough for a shart to lurk in the harbor, for people stupid enough to try to swim.\nYou are dead.")
  elif command == "w":
    print('''
The ship looks empty! You yell if someone can hear you, but nobody responds.\n
On the deck, you see three closed doors.
The (r)ed door smells like something is burning.
The (y)ellow door smells weird. You can't place the smell exactly. Not pleasant though.
The (b)lue door smells like manure.
    ''')
    command = input("Which door to open? ").lower()
    if command == "r":
      print("When you open the door, a burst of fire cooks you to the bone. Yeap. You are dead (and crusty).")
    elif command == "b":
      print("The blue door seems to be holding wild beasts. They quickly attack you and eat you to the bone. Yeap. You are dead.")
    elif command == "y":
      print("A treasure? Really? YOU WIN!")
    else:
      print("You really had to choose one of the doors. Doing anything else, resulted in the red door burning down, where a flame reaches you and the blue door breaks from the shear force of beasts that attack your burning body. The whole ship burns down along with your half eaten body.")
  else:
    print("Come on You can't do that.")  
else:
  print("Come on. You can't do that.")
  # learn about going to other places in the code
