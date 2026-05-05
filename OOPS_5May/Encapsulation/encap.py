'''Encapsulation'''
class Bank:
    __accno = 0  # Private variable:- to achieve it getter and setter lagega
    __name = ""
    __balance = 0

    def __init__(self,accno,name,bal):
        self.__accno = accno
        self.__name = name
        self.__balance = bal

    def getaccno(self):
        return self.__accno
    def setaccno(self,accno):
        self.__accno = accno

    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name = name

    def getbalance(self):
        return self.__balance
    def setbalance(self,balance):
        self.__balance = balance    
b = Bank(123,"Abhijeet",1000)
#print(b.getaccno())  # Get == getter

#  #Using getters
# print("Account No:", b.getaccno())
# b.setaccno(202)
# print(b.getaccno())

# print("Name:", b.getname())
# b.setname("Navuuu")
# print("Name:", b.getname())

# print("Balance:", b.getbalance())
# b.setbalance(7000)
# print("Balance : ",b.getbalance())
 
#print(b.__accno) # Access nhi ho paa rha hai iska answer niche
print(b._Bank__accno)


