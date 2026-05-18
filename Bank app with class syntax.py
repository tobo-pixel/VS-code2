class Bank:
  def __init__(self,owner,balance):
    self.owner = owner
    self.balance = balance
  def __str__(self):
    return f"Account owner: {self.owner}\nbalance: {self.balance} naira"
  def deposit(self,deposit_amount):
    print(f"You have successfully deposited {deposit_amount} naira")
    self.balance += deposit_amount
  def withdraw(self,withdrawal_amount):
    if withdrawal_amount > self.balance:
        print("Insufficient balance")
    else:
        print(f"You have successfully withdrawn {withdrawal_amount} naira")
        self.balance -= withdrawal_amount
  def get_balance(self):
    print(f"Your balance is {self.balance} naira")
Tobo = Bank("Tobo",25000)
print(Tobo)
print(Tobo.deposit(15000))
print(Tobo.withdraw(1000))
print(Tobo.get_balance())
