
password = 'Abhi1234'
flag = 0

for i in range(1,4):
    login = input("Enter the password : ")
    if login == password:
        print("Login Successfull")
        flag = 1
        break
    else:
        print("Wrong attempt")

if not flag:
    print("Account Locked!")        