height = int(input("Welcome to the rollercoaster!\nPlease enter your height in cm: "))

if height > 120:
  print("You are tall enough to ride!")
  age = int(input("Please enter your age: "))
  if age < 12:
    cost = 5
  elif age >= 12 and age < 18:
    cost = 7
  elif (age >= 18 and age < 45) or age > 55:
    cost = 12
  else:
    cost = 0
    print("The ride is on us, take care.")
  photos = input("Do you want photos? (default is N) ")
  if photos == "Y" or photos == "y":
    cost += 3
  print(f"The total bill is ${cost}.")
else:
  print("Sorry you cannot ride...")
