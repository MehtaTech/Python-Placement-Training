base = int(input("enter the Base price"))
demand = input("Demand high or low : ")
weekend = input("Is their weekend (yes/no) : ")


if demand == 'high' and weekend == 'yes':
    base = base * 1.3
elif demand == 'high':
    base = base * 1.2
elif weekend == 'yes':
    base = base * 1.10
else:
    print("Wrong input")

print("Final price is ",base)            