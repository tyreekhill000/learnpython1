import random
from data import data
from art import logo,vs

def format_acount(acount):
  name = acount['name']
  description = acount['description']
  country = acount['country']
  return f"{name}, {description}, from {country}"
print(logo)
acount_a = random.choice(data)
acount_b = random.choice(data)
if acount_a == acount_b:
    acount_b = random.choice(data)
print(f"Compare A: {format_acount(acount_a)}")

print(vs)

print(f"Against B: {format_acount(acount_b)}")