import random
Number = random.randint(1,10)
Attempts = 5
print("You have 5 attempts")
while Attempts > 0:
    try:
      Guess = int(input("Guess a number between 1 and 10(both inclusive): "))
    except ValueError:
      print("Enter numbers only")
    if Number != Guess and Attempts > 0:
      high = Number + 6
      low = Number - 6
      if Guess <= high and Guess >= low:
        Attempts -= 1
        print("YOUR`RE WRONG")
        print(f"You have {Attempts} attempts left")
      elif Guess > high:
         Attempts -= 1
         print("Too High")
         print(f"You have {Attempts} attempts left")
      elif Guess < low:
         Attempts -= 1
         print("TOO LOW")
         print(f"You have {Attempts} attempts left")
    elif Number == Guess:
        print("CORRECT, YOU WIN")
        break
else:
  print(f"GAME OVER\nThe number was {Number}")
