class TravelAgencies:
    __regno = 0
    __agencyname = ""
    __packagetype = ""
    __price = 0
    __flghtfacility = False

    def __init__(self, regno, agencyname, packagetype, price, flightfacility):
        self.__regno = regno
        self.__agencyname = agencyname
        self.__packagetype = packagetype
        self.__price = price
        self.__flghtfacility = flightfacility

    
    # getter methods to access the value of private variables
    def getregno(self):
        return self.__regno
    
    def getagencyname(self):
        return self.__agencyname
    
    def getpackagetype(self):
        return self.__packagetype
    
    def getprice(self):
        return self.__price
    
    def getflightfacility(self):
        return self.__flghtfacility


    # setter methods to set the value of private variables
    def setregno(self,regno):
        self.__regno = regno

    def setagencyname(self,agencyname):
        self.__agencyname = agencyname      
        
    def setpackagetype(self,packagetype):
        self.__packagetype = packagetype    
        
    def setprice(self,price):
        self.__price = price
    
    def setflightfacility(self,flghtfacility):
        self.__flghtfacility = flghtfacility
            
        
class Solution:
    
    @staticmethod
    def findagencywithhighestpackageprice(lst):
        max_price = 0
        for agency in lst:
            if agency.getprice() > max_price:
                max_price = agency.getprice()
        
        return max_price        
    
    @staticmethod    
    def agencyRetailsforGivenIdandType(lst,regno,packagetype):
        for agency in lst:
            if agency.getflightfacility() and agency.getregno() == regno and agency.getpackagetype() == packagetype:
                return agency
        return None            
    
if __name__ == "__main__":
    n = int(input("Enter the number of travel agencies: "))
    lst = []
    for i in range(n):
        regno = int(input("Enter regn no: "))
        agencyname = input("Enter agency name: ")
        packagetype = input("Enter package type: ")
        price = int(input("Enter package price: "))
        flightfacility = bool(input("Enter flight facility (True/False): "))

        agency = TravelAgencies(regno, agencyname, packagetype, price, flightfacility)
        lst.append(agency)


    print("----------")
    regno = int(input("Enter regn no: "))
    packagetype = input("Enter package type: ")

    print("-------------\n output \n-----------------")
    max_price = Solution.findagencywithhighestpackageprice(lst)
    agency = Solution.agencyRetailsforGivenIdandType(lst,regno,packagetype)
            
    print(max_price)
    print(agency.getagencyname(),":",agency.getprice())