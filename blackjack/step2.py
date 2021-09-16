import random
def deal_card():
  """This function will deal random cards for you"""
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  return random.choice(cards)


def check_for_blackjack(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return True
  else:
    return False
  
user_cards = []
dealer_cards = []
for _ in range(2):
  dealer_cards.append(deal_card())
  user_cards.append(deal_card())
print(user_cards)
print(dealer_cards)

if check_for_blackjack(dealer_cards) == True:
  print("You lost, the computer won")
elif check_for_blackjack(user_cards) == True:
  print("You won")

