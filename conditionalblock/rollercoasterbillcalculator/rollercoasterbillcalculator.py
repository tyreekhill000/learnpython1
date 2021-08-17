print("I will tell you if you can ride a roller coaster and the cost")
height_cm = int(input("Height in cm: "))
bill = 0
if(height_cm >= 120 ):
  print("you can ride the roller coaster")
  age = int(input("Your age: "))
  pic_yes_no = input("Do you want a photo(enter in smaller case)")
  if(pic_yes_no == "yes"):
    bill = bill + 3
  else:
    bill = bill + 0 
  if(age > 18):
    if(age >= 45 and age <= 55):
      bill = bill + 0
    else:
      bill = bill + 12
  elif(age >= 12 and age <= 18):
    bill = bill + 7
  else:
    bill = bill + 5
else:
  print("You can not ride the roller coaster")

print(f"Your Final cost is ${bill}")