avail = 0
seats = int(input("Seats Required : "))
vip = input("Enter VIP Status(yes/no) ")

if vip.lower() == 'yes' or seats<= avail:
    print("ticket Confirmed")
else:
    print("Waiting ")    