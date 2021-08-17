import math
#Write your code below this line 👇
def paint_calc(height, width, cover):
  area = height*width
  cans_needed = area/cover
  final_cans_needed = int(math.ceil(cans_needed))

  print(f"The final number of cans needed are {final_cans_needed}")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)