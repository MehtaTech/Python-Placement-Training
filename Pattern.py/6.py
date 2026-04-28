n = int(input("Enter number of rows: "))

for i in range(1, n+1):
    for j in range(i):
        print(chr(97 + j), end=" ")   # 65 = 'A'
    print()
