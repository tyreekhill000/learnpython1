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

operation = {"+":add, "-":subtract, "*":multiply, "/":divide}
n1 = int(input("Enter your first number: "))
for key in operation:
  print(key)
# operation_symbol = input("choose one of the symbols above:  ")
# calculation = operation[operation_symbol]
# answer = calculation(n1,n2)
# print(f"{n1} {operation_symbol} {n2} = {answer}")


can_continue = True
while can_continue:
  operation_symbol = input("choose one of the symbols above:  ")
  n2 = int(input(f"choose another number to {operation[operation_symbol].__name__} with {n1} : "))
  calculation = operation[operation_symbol]
  answer = calculation(n1,n2)
  print(f"{n1} {operation_symbol} {n2} = {answer}")
  moreoperations = input(f"If you want to do more operations with {answer} enter y if u want to start a new one, enter n: ")
  if moreoperations == "y":
     n1 = answer
     can_continue = True
  else:
    can_continue = False