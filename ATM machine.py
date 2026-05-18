print("Welcome to COS ATM machine")
store = {"14263784":["0876",30000],
         "09826363":["5253",58500],
         "23864128":["1123",7000],         
         "98327781":["1234",600]}
while True:
    account_number = input("Input your account number: ")
    if account_number in store:
        PIN = input("What is your four-digit PIN: ")
        i = 5
        while i>0 and PIN != store[account_number][0]:
            PIN = input(f"This PIN is incorrect\nYou have {i} attempts left\nTry again\n")
            i -= 1
            if i == 0:
                print("You have no attempts left")
                break
        else:
            account_balance = store[account_number][1]
            decision = input("What do you want to do\n1. Check account balance\n2. Withdraw\n3. Deposit\n4. Exit\n")
            if decision == "1":
                from ATM_functions import balance
                balance(account_balance)
            elif decision == "2":
                from ATM_functions import withdraw
                withdraw(store,account_number,account_balance)
            elif decision == "3":
                from ATM_functions import deposit
                deposit(store,account_number)
            else:
                from ATM_functions import exit
                exit()
    else:
        print("Sorry, you don`t seem to have an account")
        
    