class Phone:
    def __init__(self, phoneid, os, brand, price):
        self.__phoneid = phoneid
        self.__os = os
        self.__brand = brand
        self.__price = price 

    # Getters
    def getphoneid(self):
        return self.__phoneid
    
    def getos(self):
        return self.__os
    
    def getbrand(self):
        return self.__brand
    
    def getprice(self):
        return self.__price
    
    # Setters
    def setphoneid(self, phoneid):
        self.__phoneid = phoneid

    def setos(self, os):
        self.__os = os

    def setbrand(self, brand):
        self.__brand = brand 

    def setprice(self, price):
        self.__price = price


class Solution:
    @staticmethod
    def findPriceForGivenBrand(lst, brand):
        total = 0
        for phone in lst:
            if phone.getbrand().lower() == brand.lower():
                total += phone.getprice()
        return total

    @staticmethod
    def getPhoneIdBasedOnOs(lst, os):
        for phone in lst:
            if phone.getos().lower() == os.lower() and phone.getprice() >= 50000:
                return phone
        return None
    

if __name__ == "__main__":
    n = int(input())  # number of phones
    phones = []
    for i in range(n):
        phoneId = int(input())
        os = input().strip()
        brand = input().strip()
        price = int(input())
       
        p = Phone(phoneId, os, brand, price)
        phones.append(p)
       
    brand = input().strip()
    os = input().strip()

    # Call static methods
    totalPrice = Solution.findPriceForGivenBrand(phones, brand)
    if totalPrice > 0:
        print(totalPrice)
    else:
        print("The given Brand is not available")

    result = Solution.getPhoneIdBasedOnOs(phones, os)
    if result:
        print(result.getphoneid())
    else:
        print("No phones are available with specified os and price range")
