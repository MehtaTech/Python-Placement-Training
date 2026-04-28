password = input("Enter your password")
hasupper = False
hasdigit = False
hasSymbol = False
haslen=len(password)>=8
for i in password:
    if i.isupper():
        hasupper = True
    elif i.isdigit():
        hasdigit = True
    elif i.islower():     # For bypass
        haslower = True
    else:
        hasSymbol = True

if hasSymbol and hasdigit and hasupper and haslen:
    print("Strong")
else:
    print("Weak")    

