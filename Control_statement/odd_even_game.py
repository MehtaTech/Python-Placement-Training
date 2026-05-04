num = int(input("Enter the numbers : "))
even,odd = 0,0

while(num):
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    
    num = int(input("Enter the number "))

print("even count : ",even) 
print("Odd count ",odd)   