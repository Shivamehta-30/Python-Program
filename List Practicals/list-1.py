list1=[]
user='yes'
while user=='yes':
    list1.append(int(input("Enter value")))
    user = input("Do you want add any value in list?")
print(list1)

list1.append(int(input("Enter any value")))
print(list1)
print("Last element of list:",list1[-1])

list2=[56,5,45,100,23,14]
list2.reverse()
print("Reverse list:",list2)

no=int(input("Enter no:"))
if no in list2:
    print(no," is in the list")
else :
    print(no," is not in the list")
print("Count of number",list2.count(int(input("Give the number"))))
list2.remove(list2[-1])
list2.remove(list2[0])
list2.sort()
print(list2)

list3=[1,2,3,6,90,5]
for value in list3:
    if value<5:
        print(value)

    #1