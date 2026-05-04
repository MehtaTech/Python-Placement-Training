print("Welcome to the vending machine!")
tray1 = ["Lays","Pringles","Kurkure","Tedhe Medhe","Uncle Chips"]
tray3 = ["Dairy-Milk","Amul","Toblerone","5 Stars","Bournville"]
tray2 = ["Coke","Fanta","Limca","Campa","Sprite"]

cart = 0

while True:
    print("Tray 1:",tray1)
    print("Tray 2:",tray2)
    print("Tray 3:",tray3)
    select = int(input("Select the tray(1/2/3/0): "))
    if select == 0:
        break
    while select != 0:
        match select:
            case 1:
                for i in tray1:
                    print(i)
            case 2:
                for i in tray2:
                    print(i)
            case 3:
                for i in tray3:
                    print(i)

        item = int(input("Choose an item: "))
        cart += 1
        ask = input("Want to stay on the same tray(y/n): ")
        if ask == "y":
            pass
        else:
            break

print("total items in cart: ",cart)