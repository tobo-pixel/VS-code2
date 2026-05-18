def bankapp(accounts,fine):
  import random
  not_paid = True
  while not_paid:
    try:
      decision = input("What would u like to do?\n1. Sign up\n2. Log in\n")
      if decision == "1":
        print("What is your name")
        surname = input("Surname: ")
        firstname = input("First name: ")
        other_names = input("Other names: ")
        name = surname+" "+firstname+" "+other_names
        from Password_checker import password_checker
        password = input("Set up a strong password for your account\nPassword must have at least: 8 characters, 1 lowercase, 1 upper case, 1 special character:\n")
        password_checker(password) 
        account_number = random.randint(1000000000,9999999999)
        while account_number in accounts:
          account_number = random.randint(1000000000,9999999999)
        else:
          print(f"Welcome to Tobo Bank {name}\nYour account number is {account_number}")
          account_list = [name,0,password]
          accounts[account_number] = account_list
      elif decision == "2":
        person_account = int(input("Enter your account number: "))
        if person_account in accounts:
          person_password = input("What is your password: ")
          if person_password == accounts[person_account][2]:
            print(f"Welcome Back {accounts[person_account][0]}")
            person_decision = input("What do you want to do\n1. Deposit\n2. Payment of fine\n")
            if person_decision == "1":
              from ATM_functions import deposit
              deposit(accounts,person_account)
            elif person_decision == "2":
              if accounts[person_account][1] > fine:
                accounts[person_account][1] -= fine
                print(f"Payment of {fine} naira successful\nYou are now fine free")
                not_paid = False
            else:
              print("Choose between the options above")
          else:
            attempts = 5
            while attempts > 0 and person_password != accounts[person_account][2]:
                PIN = input(f"The password you entered is incorrect\nYou have {attempts} attempts left\n")
                attempts -= 1
                if attempts == 0:
                    print("You have no attempts left")
                    break
        else:
          print("This account number doesn't exist")
      else:
        print("Choose between the two options provided")
    except ValueError:
      print("Wrong Input")