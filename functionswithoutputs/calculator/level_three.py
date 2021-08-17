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

  
operation_symbol = input("choose one of the symbols:  ")
anothernumber = int(input("choose another number: "))
calculation = operation[operation_symbol]
nextanswer = calculation(answer,anothernumber)
print(f"{answer}{operation_symbol}{anothernumber} = {nextanswer}")


