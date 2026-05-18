students = {}
n = int(input("How many students? "))
i = 0
while i < n:
    name = input("Student's name: ")
    score = float(input(f"{name}'s score: "))
    students[name] = score
    i += 1
highest_score = max(students.values())
average_score = sum(students.values())/n
sorted_names = sorted(students,key = lambda x:x)
print("Highest score =",highest_score)
print("Average score =",average_score)
for name in sorted_names:
    print(name)  

