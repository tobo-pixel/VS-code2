print("A quadratic equation in the form ax^2 + bx + c")
a = float(input("Your a is "))
b = float(input("Your b is "))
c = float(input("Your c is "))
D = pow(b,2) - 4*a*c
if D > 0:
    first_root = (-b + pow(D,0.5))/2*a
    second_root = (-b - pow(D,0.5))/2*a
    print(f"The roots of the equation are {first_root} and {second_root}")
elif D == 0:
    root = (-b)/2*a
    print(f"The root of the equation is {root}")
else:
    print("This equation has no real solutions")