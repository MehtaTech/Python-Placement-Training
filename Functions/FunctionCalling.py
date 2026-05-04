'''Call by value'''
def update(value):
    value = 10
    print(value)
v = 5
update(v)
print(v)
 
'''call by reference'''
def updatee(lst):
    lst[0] = 21

lst = [10, 20, 30,40, 50]    
updatee(lst)
print(lst)