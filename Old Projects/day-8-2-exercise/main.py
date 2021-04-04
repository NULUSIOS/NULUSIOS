#Write your code below this line 👇

import math

def prime_checker(number):
  upper_test = round(math.sqrt(number))
  is_prime = True
  finished = False
  test = 2
  print(upper_test)
  while not finished:
    print(test)
    if test <= upper_test:
      if number % test == 0:
        is_prime = False
        finished = True
      else:
        test += 1
    else:
      finished = True
  if is_prime == True:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
