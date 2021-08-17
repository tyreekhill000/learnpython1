from art import logo
from replit import clear
print(logo)
def highest_bidder(bid):
  highest_number = 0
  highest_bidder = "dummy"
  for bids in bid:
    money = bid[bids]
    if money > highest_number:
      highest_number = money
      highest_bidder = bids
  print(f"The highest bidder is {highest_bidder} with {highest_number} Rupees ")
nameandbid = {}

bidcontinues = True
while bidcontinues:
  biddername = input("what is your name?\n")
  bidprice = int(input("what is your bid price?\n"))
  nameandbid[biddername] = bidprice
  morepeople = input("Are there more people? \n")
  if morepeople=="yes":
    clear()
  else:
    bidcontinues = False
print(nameandbid)
highest_bidder(nameandbid)
