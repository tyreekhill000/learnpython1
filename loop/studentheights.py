# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split(",")
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
total_height = 0
count = 0
for height in student_heights:
  total_height = total_height + height
  count = count + 1
print(total_height)
print(count)
average = round(total_height / count)
print(f"Your average is {average}")



#Write your code below this row 👇