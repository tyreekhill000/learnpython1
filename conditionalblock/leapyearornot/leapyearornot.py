print("I will tell you if a year is a leap year or not")
year = int(input("Enter the year: "))
if(year % 4 == 0):
  if(year % 100 == 0):
    if(year % 400 == 0 ):
      print(f"{year} is a leap year")
    else:
      print(f"{year} is not a leap year")
  else:
    print(f"{year} is a leap year")
else:
  print(f"{year} is not a leap year")



# elif(year % 100 == 0 and year % 400 == 0):
#   print(f"{year} is a leap year")
