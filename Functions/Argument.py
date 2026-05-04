'''1. Positional Argument : Jis posiion par diya hai usi position par aana chahiye, agar name ki 
jagah pehle age dede toh name mein 21 and age mein bittu aayega
'''

def profile(name, age):
    print(name, age)

profile("Bittu",21)    

'''2. Default Argument: '''
def profilee(name,age,alive="yes"):
    print("Name : ",name)   
    print("Age : ",age)
    print("Alive : ",alive)
    print(name,age,alive)
profilee("Bittu",21)
profilee("Chintu",99,"No")

'''3. Keyword Arguments : order change nhi kiya but keyword ka use kiya while giving the input '''
def profille(name,age):
    print("Name : ",name)   
    print("Age : ",age)
    print(name,age)
profille(age=56,name = "Mathu")

'''4. Multiple Arguments(*args) : '''
def add(*num):
    sum = 0
    for i in num:
        sum += i
    print(sum)

add(5,10)    

'''Multiple Keyword Arguments (** kwargs)'''
def pprofile(**data):
    for i in data:
        print(data[i])

pprofile(name="Bantu",age=69,phone="9368527410")