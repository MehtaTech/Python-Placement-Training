s = "Hey How are You guys !!!"
#print(s[:17]+s[17:])
#print(s[:-17]+s[-17:])
#print(s[-9:-4:1])
print(s[4:3:-2])

'''Palindrome'''
def palindrome(s):
    n = len(s)
    for i in range(0,(n-1)//2+1):
        if s[i] != s[n-1-i]:
            print("Not Palindrome")
            return
    print("Palindrome String")    

print(palindrome('madam'))