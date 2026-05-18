n = int(input("How many numbers do you want to square? "))
i = 0
number_list = []
while i < n:
    number = float(input("Input yur number: "))
    number_list.append(number)
    i += 1
squared_number = list(map(lambda x:x**2,number_list))
print(squared_number)