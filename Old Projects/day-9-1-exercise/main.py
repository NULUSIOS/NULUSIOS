student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for idx in student_scores:
  if student_scores[idx] > 90:
    student_grades[idx] = "Outstanding"
  elif student_scores[idx] > 80:
    student_grades[idx] = "Exceeds Expectations"
  elif student_scores[idx] > 70:
    student_grades[idx] = "Acceptable"
  else:
    student_grades[idx] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)





