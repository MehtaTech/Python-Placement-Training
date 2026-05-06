'''Find the longest subarray with sum = k'''
'''Find the longest sub array with sum <= k'''
lst = [1,2,1,0,1,1,0]
k = int(input())
l = 0
sum = 0
max = 0
for r in range(len(lst)):
    sum += lst[r]
    if sum==k and r-l+1>max:
        max = r-l+1
    while sum>k:
        sum -= lst[l]
        l += 1

print(max)
