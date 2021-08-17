import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
easyorhard = input("would you like a ")
password = ""

password_list = []
for letter in range(0,nr_letters):
  randomletter = random.choice(letters)
  password = password + randomletter
  password_list.append(randomletter)

for number in range(0,nr_numbers):
  randomnumber = random.choice(numbers)
  password = password + randomnumber
  password_list.append(randomnumber)

for symbol in range(0,nr_symbols):
  randomsymbol = random.choice(symbols)
  password = password + randomsymbol
  password_list.append(randomsymbol)
print(password)
# print(password_list)
((random.shuffle(password_list)))
# print(password_list)
jumblepass = ""
for password in password_list:
  jumblepass = jumblepass + password
print(jumblepass)
