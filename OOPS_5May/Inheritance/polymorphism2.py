class A:
    def start(self):
        print("A Started ")

class B(A):
    def start(self):
        '''Method Overriding''' 
        super().start() # iske through parent ko pehle ride karaya iske bina B Started aata sirf
        print("B Started")

if __name__ == "__main__":
    b = B()
    b.start() 
