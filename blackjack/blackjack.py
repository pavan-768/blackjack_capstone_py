import art

import os
import random

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)
  
def calculate_score(list_of_cards):        
  if list_of_cards == [11,10] or list_of_cards == [10,11]:
    return 0
  for i in list_of_cards:
      if i == 11 and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
  return sum(list_of_cards)
  
def play_game():
  print(art.logo)
  user_cards = []
  computer_cards = []
  game_over = False
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f'your cards: {user_cards},current score: {user_score}')
    print(f'computer first card: {computer_cards[0]}')
  
    if  user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      new_card = input("Do yoo want to draw another card type 'y' or type 'n' to stop: ").lower()
      if new_card == 'y':
        user_cards.append(deal_card())
      else:
        break
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
    print(f'computer cards: {computer_cards},computer score: {computer_score}')
    break
  def compare(user_score, computer_score):
    if user_score == computer_score:
      print("It's Draw")
    elif computer_score == 0:
      print("Commputer wins!!!")
    elif user_score == 0:
      print("User Wins!!!")
    elif user_score > 21:
      print("Commputer wins!!!")
    elif computer_score > 21:
      print("User Wins!!!")
    else:
      if user_score > computer_score:
        print("user wins")
      else:
        print("computer wins")
  compare(user_score,computer_score)
  

while input("Do you want to play game y or n: ").lower()== 'y':
  os.system('cls')
  play_game()

print("Thank  you for playing")



