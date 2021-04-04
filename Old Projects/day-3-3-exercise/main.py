# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
  # first test shows leap
  if year % 100 == 0:
    # second test shows not leap
    if year % 400 == 0:
      # last test shows LEAP
      print("Year is LEAP.")
    else:
      print("Year is NOT LEAP.")
  else:
    print("Year is LEAP.")
else:
  print("Year is NOT LEAP.")

