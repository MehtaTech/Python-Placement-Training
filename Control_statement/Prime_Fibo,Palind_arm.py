print("Choose an option:")
print("1. Prime Check")
print("2. Palindrome Check")
print("3. Armstrong Check")
print("4. Fibonacci Series")

choice = int(input("Enter your choice: "))
num = int(input("Enter a number: "))

# Prime Check
if choice == 1:
    prime = True
    if num < 2:
        prime = False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                prime = False
                break
    if prime:
        print(num, "is Prime")
    else:
        print(num, "is not Prime")

# Palindrome Check
elif choice == 2:
    if str(num) == str(num)[::-1]:
        print(num, "is Palindrome")
    else:
        print(num, "is not Palindrome")

# Armstrong Check
elif choice == 3:
    temp = num
    power = len(str(num))
    sum_of_powers = 0
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** power
        temp //= 10
    if sum_of_powers == num:
        print(num, "is Armstrong")
    else:
        print(num, "is not Armstrong")

# Fibonacci Series
elif choice == 4:
    n = num   # here num = how many terms
    a, b = 0, 1
    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
else:
    print("Invalid choice")
