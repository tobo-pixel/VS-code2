Number = 1
while Number > 0:
    Number = int(input("Write a number to see if it is even or odd"))
    if Number % 2 == 0:
      print("EVEN NUMBER")
    elif Number % 2 == 1:
      print("ODD NUMBER")
    else:
      print("NUMBER DOESN`T EXIST")
