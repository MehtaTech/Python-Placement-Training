'''  Multiple Inheritance'''
from abc import ABC,abstractmethod
class Animal(ABC):
    def sound(self):
        print("Gutur gu.... from aminmal")

    '''Ek abstract class ko dusri abstract class mein kar sakte hai'''

class Bird(ABC):
    @abstractmethod
    def sound(self):
        print("koo...koo...")# ye print nhi hoga as MRO: methodresoltuion order follow karta hai pehle uss class mein search karo yani pigeon   
    @abstractmethod
    def fly():
        pass
    
class Pigeon(Animal,Bird):
   
    def fly(self):
        print("Flying....")

p = Pigeon()
p.sound()
p.fly()