list=[]
for i in range(int(input("How many number you want to print:"))):
    a=(int(input("Enter number between 1-12:")))
    if a>=1 and a<=12:
        list.append(a)
    if list[i]>10:
         list[i]=10
print(list)
#4