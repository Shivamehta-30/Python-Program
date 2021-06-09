list=[]
count=0
max=0
for i in range(int(input("How many times you want to print series?="))):
    import random
    list.append((random.randint(0,1)))
    if list[i]!=0:
        count=0
    else:
        count+=1
        max=count
print(list)
print("Total zero",max)