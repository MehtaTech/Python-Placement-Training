speed = int(input("enter the speed of vehicle "))
repeated = (input("Repeated(yes/no) : "))
fine = 0

if speed > 100:
    if repeated.lower() == 'yes':
        fine = 1000*2
    else:
        fine = 1000    
elif speed > 80:
        if repeated.lower() == 'yes':
            fine = 500*2
        else:
            fine = 500      

print("Fine : ",fine)            