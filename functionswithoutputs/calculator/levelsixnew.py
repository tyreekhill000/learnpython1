from replit import clear
from art import logo
def add(n1,n2):
  """This will add two numbers"""
  return n1+n2
def subtract(n1,n2):
  """This will subtract two numbers"""
  return n1-n2
def multiply(n1,n2):
  """This will multiply two numbers"""
  return n1*n2
def divide(n1,n2):
  """This will divide two numbers"""
  return n1/n2

operation = {"+":add,"-":subtract,"*":multiply,"/":divide}

def calculator():
  can_continue = True
  print(logo)
  n1 = int(input("Enter your first number: "))
  for key in operation:
    print(key)
  while can_continue:
    operation_symbol = input("choose a symbol from above: ")
    calculation = operation[operation_symbol]
    n2 = int(input(f"Choose a number that you want to {calculation.__name__} with {n1}: "))
    answer = calculation(n1,n2)
    print(f"{n1} {operation_symbol} {n2} = {answer}")
    moreoperation = input(f"If you want to do more operations with {answer} type y if you want to start a new one type n ")
    if moreoperation == "y":
      n1 = answer
    elif moreoperation == "n":
      can_continue = False
      clear()
      calculator()
    else:
      clear()
      exit()
calculator()