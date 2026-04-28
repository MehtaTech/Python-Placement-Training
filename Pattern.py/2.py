n = int(input("Enter a number : "))

for i in range(1,n+1):
    for j in range(1, 2*i):    # 2*i-1, -1 nhi kiya as ek kam hi chalta hai
        print("*", end=" ")
    print()    