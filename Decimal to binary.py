print("This is a binary to decimal conersion calculator")
binary_value = input("Insert your binary value: ")
while not set(binary_value).issubset({'0','1'}):
    print("This isn`t a binary number")
    binary_value = input("Insert a binary number: ")
decimal_value = int(binary_value,2)
print(f"{binary_value} in decimal is {decimal_value}")
    

  