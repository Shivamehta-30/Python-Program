b=0
c=0
user='yes'
while user=='yes':
    a=int(input("Enter the values"))
    if b>a:
       b=a
    if c<a:
       c=a
    user = input("Do you want to add any value:")

print("Maximum value",b)
print("Minimum value",c)
