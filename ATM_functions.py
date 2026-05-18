def balance(account_balance):
  print(f"YOUR ACCOUNT BALANCE IS {account_balance} Naira")


def withdraw(dict1,account_number,account_balance):
  try:
    withdrawal_amount = int(input("How much do you want to withdraw: NGN "))
    if withdrawal_amount < 0:
      print("Invalid input")
    else:
      if withdrawal_amount > int(account_balance):
        print("INSUFFICIENT BALANCE")
      else:
        print(f"YOU HAVE WITHDRAWN {withdrawal_amount} Naira")
        dict1[account_number][1] -= withdrawal_amount
  except ValueError:
    print("Invalid input")


def deposit(dict1,account_number):
  try:
    deposit_amount = int(input("How much do you want to deposit: NGN "))
    if deposit_amount < 0:
      print("Ivalid input")
    else:
      dict1[account_number][1] += deposit_amount
      print(f"YOU HAVE SUCCESSFULLY DEPOSITED {deposit_amount} Naira")
  except ValueError:
    print("Invalid input")
 
 
def exit():
  print("Thank you for using COS atm bank")
  
 

