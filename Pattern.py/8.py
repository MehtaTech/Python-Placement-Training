n = int(input("Enter number of rows: "))

for i in range(1, n+1):
    for k in range(1,n-i+1): # n-i+1 yu toh n-i par ek lena padta hai python mein
        print(" ",end="")
    for j in range(1, i+1):
        print("*", end=" ")    
    print()    