import random
from data import data
from art import logo
print(logo)
acount_a = random.choice(data)
acount_b = random.choice(data)
if acount_a == acount_b:
    acount_b = random.choice(data)
# print(acount_a['name'])
# print(acount_a['description'])