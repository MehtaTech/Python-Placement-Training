amount = int(input("Enter the amount : "))
premium = input("User premium(yes/no) : ")

if amount >= 5000:
    amount = amount * 0.8
elif amount >= 3000:
    amount = amount * 0.9
else:
    print("Invalid choice")


if premium == 'yes':
    amount = amount * 0.95
print("Total amount to be paid : ",amount)