import random
def deal_card():
  """This function will deal random cards for you"""
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  return random.choice(cards)


def calculate_score(cards):
  sum_cards = sum(cards)
  if sum_cards == 21 and len(cards) == 2:
    return 0
  elif sum_cards > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
    return sum(cards)
  else:
    return sum_cards

is_game_over = False 
user_cards = []
dealer_cards = []
for _ in range(2):
  dealer_cards.append(deal_card())
  user_cards.append(deal_card())

  dealer_score = calculate_score(dealer_cards)
  user_score = calculate_score(user_cards)
  print(f"Your cards are {user_cards}, current score is: {user_score}")
  print(f"Computers first card: {dealer_cards[0]}")
 


