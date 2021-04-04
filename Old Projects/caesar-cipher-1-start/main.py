alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' (default) to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(original_text, shift_ammount):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
  
  if shift_ammount > 26:
    shift_ammount = shift_ammount % 26

  ## MINE IS ONE LINE LESS
  # text_new = list(original_text)
  # for pos_in_text in range(len(original_text)):
  #   pos_in_alphabet = alphabet.index(original_text[pos_in_text])
  #   new_pos = pos_in_alphabet + shift_ammount
  #   if new_pos > 25:
  #     new_pos -= 26
  #   # print(text_list)
  #   # print(pos_in_alphabet)
  #   # print(new_pos)
  #   text_list[pos_in_text] = alphabet[new_pos]

  text_new = ""
  for letter in original_text:
    pos_in_alphabet = alphabet.index(letter)
    new_pos = pos_in_alphabet + shift_ammount
    if new_pos > 25:
      new_pos -= 26
    new_letter = alphabet[new_pos]
    text_new += new_letter

  # print(''.join(text_new))
  print(text_new)
   
    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

if direction == "encode":
  print("Here is the encoded message")
  encrypt(text, shift)
