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
n2 = int(input("Enter your second number: "))
for key in operation:
  print(key)
operation_symbol = input("choose one of the symbols above:  ")
calculation = operation[operation_symbol]
answer = calculation(n1,n2)
print(f"{n1} {operation_symbol} {n2} = {answer}")

nextanswer = answer
can_continue = True
while can_continue:
  moreoperations = input("If you want to do more operations enter y if u want to start a new one, enter n: ")
  if moreoperations == "y":
    operation_symbol = input("choose one of the symbols:  ")
    anothernumber = int(input(f"choose another number to {operation[operation_symbol].__name__} with {nextanswer} : "))
    calculation = operation[operation_symbol]
    print(f"{nextanswer}{operation_symbol}{anothernumber} = ")
    nextanswer = calculation(nextanswer,anothernumber)
    print(nextanswer) 
  else:
    can_continue = False
