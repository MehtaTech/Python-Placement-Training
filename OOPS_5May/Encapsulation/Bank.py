'''Class in Python'''
class Bank:
    accno = 52642
    name = "Abhijeet"

    def show(self):
        print("Account number : ",self.accno)
        print("Name : ",self.name)

b = Bank()
# print(b.name)
b.show()
print