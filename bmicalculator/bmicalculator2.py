print("I will tell you your BMI")

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
height_float = float(height)
weight_float = float(weight)
bmi = round(weight_float/height_float**2,2)
print(bmi)

if(bmi < 18.5):
  print(f"Your BMI is {bmi}, you are underweight.")
elif(bmi > 18.5 and bmi < 25):
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif(bmi > 25 and bmi < 30):
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif(bmi > 30 and bmi < 35):
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")






"Your BMI is 18, you are underweight."
"Your BMI is 22, you have a normal weight."
"Your BMI is 28, you are slightly overweight."
"Your BMI is 33, you are obese."
"Your BMI is 40, you are clinically obese."