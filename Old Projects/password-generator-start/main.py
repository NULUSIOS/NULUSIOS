#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

passwd_list = []

for letter in range(1, nr_letters + 1):
  # passwd += letters[random.randint(0,51)]
  passwd_list += random.choice(letters)
for symbol in range(1, nr_symbols + 1):
  # passwd += symbols[random.randint(0,8)]
  passwd_list += random.choice(symbols)
for number in range(1, nr_numbers + 1):
  # passwd += numbers[random.randint(0,9)]
  passwd_list += random.choice(numbers)

random.shuffle(passwd_list)

passwd = ""

for chara in passwd_list:
  passwd += chara

print(passwd)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# passwd2 = ""
# char_types = ["letter", "symbol", "number"]
# remaining_letters = nr_letters
# remaining_symbols = nr_symbols
# remaining_numbers = nr_numbers
# total_chars = nr_letters + nr_symbols + nr_numbers

# for pass_letter in range(1, total_chars * 10):
#   char_type = random.choice(char_types)
#   print(char_type, remaining_letters, remaining_symbols, remaining_numbers)
#   if total_chars > 0:
#     if char_type == "letter" and remaining_letters > 0:
#       passwd2 += random.choice(letters)
#       remaining_letters -= 1
#       total_chars -= 1
#     elif char_type == "symbol" and remaining_symbols > 0:
#       passwd2 += random.choice(symbols)
#       remaining_symbols -= 1
#       total_chars -= 1
#     elif char_type == "number" and remaining_numbers > 0:
#       passwd2 += random.choice(numbers)
#       remaining_numbers -= 1
#       total_chars -= 1
#     else:
#       print("RETRY!")
#   else:
#     print(passwd2)
#     break

