print("Let's calculate your cgpa")
try:
  n_of_courses = int(input("How many courses are you offering: "))
except ValueError:
  print("Invalid input")
i = 0
total_units = 0
total_weighed_gp = 0
while i < n_of_courses:
  course_code = input("What is the course code: ")
  try:
    units = int(input(f"How many units is {course_code}: "))
    grade = float(input(f"What was your score in {course_code}(over 100): "))
    total_units += units
    if grade >= 70:
      print("That`s an A")
      weighed_gp = 5*units
    elif grade >= 60:
      print("That`s a B")
      weighed_gp = 4*units
    elif grade >= 50:
      print("That`s a C")
      weighed_gp = 3*units
    elif grade >= 45:
      print("That`s a D")
      weighed_gp = 2*units
    elif grade >= 40:
      print("That`s an E")
      weighed_gp = 1*units
    else:
      print("Fail")
      weighed_gp = 0*units
    total_weighed_gp += weighed_gp
    i += 1
  except ValueError:
    print("Invalid input")
cgpa = total_weighed_gp/total_units
cgpa = round(cgpa,2)
if cgpa >= 4.5:
  print(f"Your CGPA is {cgpa}")
  print("FIRST CLASS DEGREE")
elif cgpa >= 3.5:
  print(f"Your CGPA is {cgpa}")
  print("SECOND CLASS UPPER DEGREE")
elif cgpa >= 2.4:
  print(f"Your CGPA is {cgpa}")
  print("SECOND CLASS LOWER DEGREE")
elif cgpa >= 1.5:
  print(f"Your CGPA is {cgpa}")
  print("THIRD CLASS DEGREE")
elif cgpa >= 1:
  print(f"Your CGPA is {cgpa}")
  print("PASS")
else:
  print(f"Your CGPA is {cgpa}")
  print("WITHDRAWAL")
