tpl = (1,2,3)
print(type(tpl))

tup1 = tuple(input())
print(type(tup1))
print(tup1)


tup1 = (1,2,3,4,5,6,7,8,9)
'''tup1.append() 
tup1.delete()
tup1.update()'''
# tuple is immutable isiliye append,update delete kuch nhi hoga

'''Sorting of tuple '''
tup2 = (5,3,6,2,8,1)
l = sorted(tup2,reverse=True)
l = sorted(tup2)
print(tup2)
print("Sorted --> ",l) # answer list mein aayega usko tuple mein convert karne ke liye niche
'''List to tuple'''
print(tuple(l))