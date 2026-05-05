from abc import ABC,abstractmethod


class Payment(ABC): #(ABC) is single level inheritence
    @abstractmethod
    def pay():
        pass

class UPI(Payment):
    def pay(self):
        print("Payment Done by UPI")

class CC(Payment):
    def pay(self):
        print("Payment Done by Credit Card")

class DC(Payment):
    def pay(self):
        print("Payment Done by Debit Card")

if __name__ == "__main__":
    u = UPI()
    u.pay()

    c = CC()
    c.pay()

    d = DC()
    c.pay()