print("Today you will play an island game to find treasure")
desision = input("would you like to go left or right: ")
if(desision == "left"):
    swim_wait = input("will you swim or wait: ")
    if(swim_wait == "wait"):
      red_blue_yellow = input("Choose a door from red, blue, or yellow: ")
      if(red_blue_yellow == "yellow"):
        print("congrats, you won!!")
      elif(red_blue_yellow == "blue"):
        print("You were eaten by beast")
      else:
        print("you were burned by fire")
    else:
      print("you got attacked by a trout")
else:
  print("you fell into a hole")