student_scores = {
  "Harry": {"class":8,"mark":81},
  "Ron": {"class":5,"mark":78},
  "Hermione": {"class":7,"mark":99}, 
  "Draco": {"class":9,"mark":74},
  "Neville": {"class":8,"mark":62},
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
student_classandgrade = {}
#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
  if student_scores[key]["mark"] >= 91 and student_scores[key]["mark"] <= 100:
    student_classandgrade["class"] = student_scores[key]["class"]
    student_classandgrade["grade"] = "outstanding"
    student_grades[key] = student_classandgrade
  elif student_scores[key]["mark"] >= 81 and student_scores[key]["mark"] <= 90:
    student_classandgrade["class"] = student_scores[key]["class"]
    student_classandgrade["grade"] = "outstanding"
    student_grades[key] = student_classandgrade
  elif student_scores[key]["mark"] >= 71 and student_scores[key]["mark"] <= 80:
    student_classandgrade["class"] = student_scores[key]["class"]
    student_classandgrade["grade"] = "outstanding"
    student_grades[key] = student_classandgrade
  elif student_scores[key]["mark"] <= 70:
    student_classandgrade["class"] = student_scores[key]["class"]
    student_classandgrade["grade"] = "outstanding"
    student_grades[key] = student_classandgrade
    

# 🚨 Don't change the code below 👇
print(student_grades)