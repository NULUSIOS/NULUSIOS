# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# pos_x = int(position) // 10
# pos_y = int(position) % 10
pos_x = int(position[0])
pos_y = int(position[1])

if pos_x > 3 or pos_x < 1 or pos_y > 3 or pos_y < 1:
  print("Hey your position is out of range!")
  # stop program here

print(f"You entered X {pos_x} and Y {pos_y}.")
pos_x -= 1
pos_y -= 1

# if pos_y == 0:
#   row1[pos_x] = "X"
# elif pos_y == 1:
#   row2[pos_x] = "X"
# elif pos_y == 2:
#   row3[pos_x] = "X"
#
# sel_pos = map[pos_y]
# sel_pos[pos_x] = "X"
# map[pos_y][pos_x] = "X"
map[int(position[1])-1][int(position[0])-1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")