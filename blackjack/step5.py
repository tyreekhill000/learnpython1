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


def compare(user_score, dealer_score):
  if user_score >21 and dealer_score>21:
    return "You went over, you lose"
  if user_score == dealer_score:
    return "You both had the same score, you draw"
  if dealer_score == 0:
    return "The computer wins, you lose"
  if user_score == 0:
    return "You win"
  if user_score>21:
    return "you went over, you lose"
  if dealer_score>21:
    return "The dealer went over, you win"
  if user_score > dealer_score:
    return "You had a higher score, you win"
  else:
    return "You lose"


is_game_over = False
user_cards = []
dealer_cards = []
for _ in range(2):
  dealer_cards.append(deal_card())
  user_cards.append(deal_card())
while not is_game_over:
  dealer_score = calculate_score(dealer_cards)
  user_score = calculate_score(user_cards)
  print(f"Your cards are {user_cards}, current score is: {user_score}")
  print(f"Computers first card: {dealer_cards[0]}")
  if dealer_score == 0 or user_cards == 0 or user_score > 21:
    is_game_over = True
  else:
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
  if another_card == "y":
    user_cards.append(deal_card())
  else:
    is_game_over = True

while dealer_score < 17 and dealer_score != 0:
  dealer_cards.append(deal_card())
  dealer_score = calculate_score(dealer_cards)



print(f"Your final hand is {user_cards}, final score {user_score} ")
print(f"The computer final hand is {dealer_cards}, final score {dealer_score}")

print(compare(user_score, dealer_score))