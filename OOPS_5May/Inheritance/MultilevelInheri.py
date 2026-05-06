'''Create a class animal in which u need to add abstract methods like speak,mode and add some default methods sleep,walk '''
from abc import ABC,abstractmethod
class Animal:
    @abstractmethod
    def sound():
        pass

    '''Ek abstract class ko dusri abstract class mein kar sakte hai'''

class Bird(Animal,ABC):
    @abstractmethod
    def fly():
        pass
    
class Pigeon(Bird):
    def sound(self):
        print("Gutur Gu... Gutur Gu")
    def fly(self):
        print("Flying....")

p = Pigeon()
p.sound()
p.fly()