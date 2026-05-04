'''
# Question : WAP to find second largest and third smallest number in a list of elements
import math

lst = eval(input("Enter the elements of list")) # eval use kiya i stead of list due to copy reasons
max, smax = lst[0], lst[0]
min, smin, tmin = math.inf,math.inf,math.inf
for i in lst:
    if i > max:
        smax = max
        max = i
    else:
        if i>smax:
            smax = i
    if i<min:
        tmin=smin
        smin=min
        min = i
    elif i<smin:
        tmin =smin
        smin = i
    elif i<tmin:
        tmin = i        



print(lst)
print("Maximum : ",max)
print("Second Maximum : ",smax)
print("Third Smallest ",tmin)
'''


'''Q2 WAP to rotate the elements in a list by k times in anticlockwise direction
[10,20,30,40,50]
input k =2
output [40,50,10,20,30]'''

'''
lst1 = eval(input("Enter list : "))
k = int(input("Enter k : "))

lst1 = lst1[k:]+lst1[:k]
print(lst1)

1 more way to solve question 2
lst2 = eval(input("Enter list : "))
k = int(input("Enter k : "))

for i in range(k):
    item = lst2.pop()
    lst2.insert(0,item)
print(lst2)    

'''

'''Q3. WAP to rotate elements by k times in anticlockwise direction keeping m elements constant at the left side

lst3 = [10,20,30,40,50,60]
k=2
m=2

for i in range(k):
    item = lst3.pop()
    lst3.insert(m, item)

print(lst3)'''
'''
#Q4 WAP to find nth largest and nth smallest number
lst5 = eval(input("Enter a list : "))
n = int(input("Enter the element : "))

lst5.sort()
print(lst5)

print(lst5[n-1])
print(lst5[-n])
'''
'''
#Q5 WAP to find second duplicate
lst6 = eval(input("Enter list : "))
element = int(input("Enter a number : "))
c = 3

for i in range(0, len(lst6)):
    if lst6[i] == element:
        c -= 1
    if c == 0:
        print(i)
        break
else:
    print("Not Exist ")    
'''
# Q7 A teacher stored marks but some entries are invalid, remove them and return valid marks
# invalid = -1
# input [45,67,-1,89,-1,76]
# output [45,67,89,76]

lst = [45, 67, -1, 89, -1, 76]
valid_marks = []
for mark in lst:
    if mark > 0:
        valid_marks.append(mark)

print("Valid marks:", valid_marks)