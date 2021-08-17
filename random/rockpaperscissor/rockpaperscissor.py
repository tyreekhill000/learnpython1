import random

rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


# Paper
paper=''''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''


scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissor]
print("today the computer will play rock paper scissors against you")
player_opt_int = int(input("Choose 0 for rock, 1 for paper, or 2 for scissors: "))
if(player_opt_int > 2 or player_opt_int < 0):
  print("please enter a valid number")
else:

  player_opt = options[player_opt_int]
  computer_opt = random.choice(options)
  print("you chose:" + player_opt)
  # comp_opt_num = random.randint(0,1,2)
  print("the computer chose:" + computer_opt)
  player_symbol = (options[player_opt_int])

  if(player_opt == computer_opt):
    print("you tied")
  elif(player_opt == rock and computer_opt == scissor):
    print("You won")
  elif(player_opt == paper and computer_opt == rock):
    print("You won")
  elif(player_opt == scissor and computer_opt == paper):
    print("You won")
  else:
    print("You lost")