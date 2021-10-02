import random
from data import data
from art import logo,vs
from replit import clear

def format_acount(acount):
  name = acount['name']
  description = acount['description']
  country = acount['country']
  return f"{name}, {description}, from {country}"

def check_answer(follower_count_a,follower_count_b,guess):
  if follower_count_a > follower_count_b:
    return guess == "a"
  else:
    return guess == "b"





print(logo)
acount_a = random.choice(data)
acount_b = random.choice(data)
if acount_a == acount_b:
    acount_b = random.choice(data)
print(f"Compare A: {format_acount(acount_a)}")

print(vs)

print(f"Against B: {format_acount(acount_b)}")
guess = input("Who has more followers? Type 'A' or 'B': ").lower()


acount_a_follow = acount_a['follower_count']
acount_b_follow = acount_b['follower_count']
# print(acount_a_follow)
# print(acount_b_follow)


answer = check_answer(acount_a_follow,acount_b_follow,guess)
if answer == True:
  print("You are correct")
else:
  print("sorry you are wrong")


# if guess == "a" and acount_a_follow > acount_b_follow:
#   score = score + 1
# elif guess == "a" and acount_a_follow < acount_b_follow:
#   game_continue = False
# elif guess == "b" and acount_a_follow < acount_b_follow: 
#   score = score + 1
# elif guess == "b" and acount_a_follow > acount_b_follow: 
#   game_continue = False
# print(score)

# if acount_a_follow > acount_b_follow:
#   if guess == "a":
#     print("correct")
#   else:
#     print("wrong")
# elif acount_a_follow < acount_b_follow:
#   if guess == "b":
#     print("correct")
#   else:
#     print("wrong")

