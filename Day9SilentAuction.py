from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print('Welcome to the secret auction program.')
user_response = 'yes'
user_bids_dict = {}

while user_response == 'yes':
  name = str(input('What is your name?: '))
  bid = int(input("What's your bid?: $"))
  user_bids_dict[name] = bid
  continue_bid = str(input("Are there any other bidders? 'yes' to continue 'no' to end\n"))
  clear()
  if continue_bid == 'no':
    user_response = 'no'

max_bid = 0
for key in user_bids_dict:
  user_bid = user_bids_dict[key]
  if user_bid > max_bid:
    max_bid = user_bid
for key in user_bids_dict:
  if user_bids_dict[key] == max_bid:
    winner = key

  
print(f' The winner of the auction is {winner}, and their bid was ${max_bid}!')
