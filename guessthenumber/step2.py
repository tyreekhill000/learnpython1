import random


def check_answer(guess, answer):
  """Checks answer against the guess"""
  if guess < answer:
    print("Too low.")
  elif guess > answer:
    print("Too high.")
  else:
    print(f"You got it! The answer was {answer}")
#choose a random number from 1 to 100
answer = random.randint(1,100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {answer}")
#make a function to set difficulty


#let user guess number
guess = int(input("Make a guess: "))
#create a funtion to check whether or not user number is the answer
check_answer(guess, answer)
#track number of turns and reduce by 1 if wrong
#Repeat guessing function if they get wrong
