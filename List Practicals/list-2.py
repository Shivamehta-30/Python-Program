import random
a=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    a.append(random.randint(1,100))
print("Random number list is: ",a)
print("Max value",max(a))
print("Min value",min(a))
print("Avg",sum(a)/n)
a.sort()
print("Second largest",a[-2])
print("Second smallest",a[1])
for value in a:
    if value%2==0:
        print("Even number",value)
#2