cash = 1000
years = 0
while cash < 5000:
    interest = 0.1 * cash
    cash += interest
    years += 1
else:
    print(f"It took {years} years to reach 5000 naira")
    cash = round(cash,1)
    print(f"Balance = {cash} naira")
