'''Wrong'''


dist = float(input("Enter the distance travelled : "))
bill = 0
night = input("Night Travel(yes/no) : ")
if dist <= 5:
    bill = 50* dist
elif dist <= 10:
    bill = 50 * 5 + (dist - 5) * 40
else:
    bill = (50 * 5) + (40 * 5) + (dist - 10)* 30

if night.lower() == 'yes':
    bill = bill * 1.2

print("Total amount : ",bill)