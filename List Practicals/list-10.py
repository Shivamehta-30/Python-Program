user='yes'
l=[]
while user=='yes':
   l.append(int(input("Enter value of n")))
   user=input("do you want to add any value?")
l=l[len(l)-1:]+l[:-1]
print("Rotated list",l)