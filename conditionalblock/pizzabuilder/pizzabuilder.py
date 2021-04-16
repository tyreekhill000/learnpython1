# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# 🚨 Don't change the code above 👆
# print(size)
# print(add_pepperoni)
# print(extra_cheese)
bill = 0
# if(size == "S"):
#   bill = 15
#   if(add_pepperoni == "Y"):
#     bill = bill + 2
# elif(size == "M"):
#   bill = 20
#   if(add_pepperoni == "Y"):
#     bill  = bill + 3
# else:
#   if(size == "L"):
#     bill = 25
#     if(add_pepperoni == "Y"):
#       bill = bill + 3
if(size == "S" and add_pepperoni == "Y"):
  bill = 17
elif(size == "S" and add_pepperoni == "N"):
  bill = 15
if((size == "M" or size =="L") and add_pepperoni == "Y"):
  add_pepperoni
  if(size == "M"):
    bill = 23
  elif(size == "L"):
    bill = 28
if(extra_cheese == "Y"):
  bill = bill + 1

print(f"{bill} is your total")

















# Small Pizza: $15 Medium Pizza: $20 Large Pizza: $25 Pepperoni for Small Pizza: +$2 Pepperoni for Medium or Large Pizza: +$3 Extra cheese for any size pizza: + $1 Example Input size = "L" add_pepperoni = "Y" extra_cheese = "N" Example Output Your final bill is: $28. e.g. When you hit run, this is what should happen: