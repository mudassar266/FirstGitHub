  # age_to_go_school = 5
  # faisal_age = int(input("Enter the age of the student "))
  # # can faisal go to school 
  # if age_to_go_school == faisal_age:
  #     print("Faisal can go to school ")
age_required = 5
student_age = int(input("Enter the stuent age ="))
# can student go to school?
if student_age == age_required:
  print("Yes! he can go to school ")
#elif student_age != age_required:
 #   print("No! student can go to school")
elif student_age <= age_required:
  print("He is too young to join the school")
elif student_age >= age_required:
  print("Student can join the school but in higher section ")
