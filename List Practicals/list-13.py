n=int(input("Enter how many number you want to add in list?"))
list=[]
list1=[]
for i in range(n):
    list.append(int(input("Enter values:")))
print(list)
for i in list:
    if i not in list1:
        list1.append(i)
print(list1)