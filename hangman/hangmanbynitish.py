from hangmanwords import word_list
from hangmanart import stages,logo
import random
# generate a random word
print(logo)
wordchoice = random.choice(word_list)
print("test word==" + wordchoice)
wordlen = len(wordchoice)
wordlist = []
# generate as many blank spaces as the word
for alphabets in range(wordlen):
  wordlist.append("_")


wordjoin = " "
wordlist_string = wordjoin.join(wordlist)
print(wordlist_string)
game_can_continue = True
lives = len(stages)
while game_can_continue:
  guess = input("Guess a letter: ")

  if(guess in wordlist):
    print(f"{guess} was alread guessed, guess another letter")

  for position in range(wordlen):
    letter = wordchoice[position]
    if(letter==guess):
      wordlist[position] = letter
  
  if(guess not in wordlist):
    lives-=1
    print(stages[lives])
    if(lives == 0):
      game_can_continue = False
      print(f"You lost, the correct answer was {wordchoice}")
  
  if("_" not in wordlist):
    game_can_continue = False
    print("You won!")

  wordlist_string = wordjoin.join(wordlist)
  print(wordlist_string)

  
