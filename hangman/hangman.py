from hangmanwords import word_list
from hangmanart import stages,logo
import random
print(logo)
wordchoice = (random.choice(word_list))
print("test word ==" + wordchoice)
wordlist = []
wordlen = len(wordchoice)
for count in range(wordlen):
  wordlist.append("_")
# print(wordlist)

wordjoin = " "
wordlist_join = wordjoin.join(wordlist)
print(wordlist_join)
game_continue = True
lives = len(stages) -1

while game_continue:
  guess = input("Guess a letter: ")
  if(guess in wordlist):
    print("this letter was already chosen, chose a different letter")
  for position in range(wordlen):
    letter = wordchoice[position]
    if(letter==guess):
      wordlist[position] = letter
  if(guess not in wordchoice):
    print(f"{guess} is not in the word and you lose a life")
    print(stages[lives])
    if(lives==0):
      print("You lost the game")
      game_continue = False
    lives-= 1

  if("_" not in wordlist):
    print("You won")
    game_continue = False
    
  wordlist_join = wordjoin.join(wordlist)
  print(wordlist_join)





