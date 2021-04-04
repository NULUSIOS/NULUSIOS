# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L (M is default) ")
add_pepperoni = input("Do you want pepperoni? Y or N (default is N) ")
extra_cheese = input("Do you want extra cheese? Y or N (default is N) ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if size == "S" or size == "s":
  price = 15
elif size == "L" or size == "l":
  price = 25
else:
  price = 20

if extra_cheese == "Y" or extra_cheese == "y":
  price += 1

if (add_pepperoni == "Y" or add_pepperoni == "y") and (size == "S" or size == "s"):
  price += 2
else:
  if add_pepperoni == "Y" or add_pepperoni == "y":
    price += 3

print(f"Your final bill is: ${price}")



