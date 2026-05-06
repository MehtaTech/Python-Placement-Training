lst = eval(input("Enter the number of vehicles pass in 1 minute : "))
k = int(input(" "))
sum, max = 0, 0

for element in range(k):
    sum += lst[element]
 
if sum>max:
    max = sum

for i in range(k,len(lst)):
    sum -= lst[i-k]
    sum += lst[i]
    if sum>max:
        max = sum
print(max)