user='yes'
l=[]
m=[]
while user=='yes':
        l.append(int(input("Enter value of n")))
        m.append(int(input("Enter value of m")))
        user=input("do you want to add any value?")

n = []
for i in range(len(l)):
        n.append(l[i]+m[i])

print(n)