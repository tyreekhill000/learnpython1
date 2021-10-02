from random import randint
from art import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
def set_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def check_answer(guess, answer,turns):
  """Checks answer against the guess"""
  if guess < answer:
    print("Too low.")
    return turns -1
  elif guess > answer:
    print("Too high.")
    return turns -1
  else:
    print(f"You got it! The answer was {answer}")
#choose a random number from 1 to 100
def game():
  print(logo)
  answer = randint(1,100)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  print(f"Pssst, the correct answer is {answer}")
  #make a function to set difficulty
  turns = set_difficulty()
  #let user guess number
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
  #create a funtion to check whether or not user number is the answer
  
    
    turns = check_answer(guess, answer, turns)


  #track number of turns and reduce by 1 if wrong
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")
  #Repeat guessing function if they get wrong
game()