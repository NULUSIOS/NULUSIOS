from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

def find_winner(bidders):
  biggest_value = 0
  for person in bidders:
    if bidders[person] > biggest_value:
      biggest_value = bidders[person]
      biggest_bidder = person
    elif bidders[person] == biggest_value:
      biggest_bidder = biggest_bidder + " + " + person
  print(f"Biggest bidder or bidders: {biggest_bidder}.\nThe winning bid was {biggest_value}.")

clear()
print(logo)

next_bidder = True
bidders = {}

while next_bidder:
  bidder = input("Please give me the bidder's name: ")
  bid = int(input("Please give the bid: "))
  next_bid = input("Type 'yes' if there is any additional bidder: ").lower()
  if next_bid == "yes":
    next_bidder = True
    clear()
  else:
    next_bidder = False
    clear()
  bidders[bidder] = bid

find_winner(bidders)
