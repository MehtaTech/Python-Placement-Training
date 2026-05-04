print("Welcome to Dhruvi Cafe!!")
o = print("Choose the Tray \n Select 1,2,3 and 0 for exit ")


order = int(input("Enter the tray number you want : "))
tray1 = ("a. Lays 25$ \n b. Uncle Chips 20$ \n c. Kurkure 10$")
if order == 1:
    print(tray1)
    item = input("select a product : ")
    if item.lower() == 'a' or 'b' or 'c':
        print("Added to Cart")
        print(o)   
    else:
        print(o)    
