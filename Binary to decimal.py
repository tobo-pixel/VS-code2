print("This is a decimal to binary conersion calculator")
decimal_value = int(input("Insert your decimal value: "))
binary_value = bin(decimal_value)[2:]
print(f"{decimal_value} in binary is {binary_value}")