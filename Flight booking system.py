seats = 100
while True:
    print("What is your name")
    surname = input("Surname: ")
    lastname = input("Last name: ")
    other_names = input("Other names: ")
    name = surname+" "+other_names+" "+lastname
    try:
        age = int(input("How old are you: "))
        tickets = int(input("How many tickets would you like to purchase: "))
        if tickets > seats:
            print("Sorry, not enough seats available")
        else:
            print(f"Booking successful for {name}\n{age} years old\n{tickets} tickets")
            seats -= tickets
    except ValueError:
        print("Error\nInput a number")