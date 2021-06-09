import random
a=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    a.append(random.randint(1,50))
print(a)
for value in a:
    value=value**2
    print(value)
b=[]
str1="abcdefghijklmnopqrstuvwxyz"
for i in range(1,len(str1)):
    c=(str1[i])*i
    b.append(c)
print(b)