amount = int(input("Enter the amount you need to withdraw : "))
balance = 50000

if amount < (balance - 1000):
    print("Transaction Complete ")
else:
    print("Transaction failed, Minimum balance violation")    