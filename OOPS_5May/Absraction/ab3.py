'''Create a class animal in which u need to add abstract methods like speak,mode and add some default methods sleep,walk '''

from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):

    # Abstract methods .
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def mode(self):
        pass

    # Default methods 
    def sleep(self):
        print("Animal is sleeping...")

    def walk(self):
        print("Animal is walking...")

# Concrete Class 1
class Dog(Animal):
    def speak(self):
        print("Dog says: Woof Woof!")

    def mode(self):
        print("Dog is domestic")

# Concrete Class 2
class Lion(Animal):
    def speak(self):
        print("Lion roars: Roooar!")

    def mode(self):
        print("Lion is wild")

# Usage
d = Dog()
d.speak()
d.mode()
d.sleep()
d.walk()

print("-----")

l = Lion()
l.speak()
l.mode()
l.sleep()
l.walk()
