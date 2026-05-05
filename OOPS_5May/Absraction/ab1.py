class Meal:
    def __cookrajma(self): # __ lagane se normal se private ho gya
        print("Rajma Prepared")
    def __cookrumaliroti(self):
        print("Roomali Roti Prepare") 
    def __cooksalad(self):
        print("Salad Prepared Prepared")
    def __cookrice(self):
        print("Rice prepared")
    def __cooksweet(self):
        print("Sweet Prepared...")   

    def cookmeal(self):
        self.__cookrajma()
        self.__cookrumaliroti()
        self.__cooksalad()
        self.__cookrice()
        self.__cooksweet()    

if __name__ == '__main__':
    m = Meal()
    m.cookmeal()
