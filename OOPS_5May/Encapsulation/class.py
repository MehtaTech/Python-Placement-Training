'''Class in Python'''
class Bank:
    accno = 0
    name = ""
    # Constructor
    def __init__(self,accno,name):  # self :Current instance of your class
        self.accno = accno
        self.name = name

    def show(self):
        print("Account number : ",self.accno)
        print("Name : ",self.name)

b = Bank(25250,"Navika")
b2 = Bank(25251,"Abhi")
# print(b.name)
b.show()   # Calling 
b2.show()  # Calling
print(b.name)