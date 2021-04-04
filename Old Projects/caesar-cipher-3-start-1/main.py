alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' (default) to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(coding_direction,plain_text, shift_amount):

  if shift_amount > 26:
    shift_amount = shift_amount % 26
  
  if coding_direction == "decode":
    shift_amount = -shift_amount

  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    if new_position > 25:
      new_position -= 26
    if new_position < 0:
      new_position += 26
    cipher_text += alphabet[new_position]
  
  print(f"The {coding_direction}d text becomes '{cipher_text}'")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(coding_direction=direction, plain_text=text, shift_amount=shift)
