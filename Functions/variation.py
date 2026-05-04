'''No return no argument'''
def greet():
    print("Good Morning")

greet()    

def greeting(name):
    print(name, "Sb khariyat")
greeting("Abhijeet")

''' Return and  No argument'''
def greetings():
    return "Sab thik hai .."
name = greetings()
print(name)

def greeting(name):
    return "Very good morning " + name

name = greeting("Abhi ")
print(name)