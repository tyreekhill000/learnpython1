#Write your code below this line 👇
def prime_checker(number):
  """This function will tell you if a number is prime or not"""
  is_prime = True
  for dividend in range(2,number):
    answer = number%dividend
    if(answer == 0):
      is_prime = False
  if(is_prime == False):
    print(f"{number} is not a prime number")
  else:
    print(f"{number} is a prime number")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)