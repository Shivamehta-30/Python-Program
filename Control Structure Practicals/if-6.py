rollno=int(input("Enter No:"))
name=input("Enter Name :")
maths=int(input("Enter Maths Marks:"))
sci=int(input("Enter sci Marks:"))
eng=int(input("Enter eng Marks:"))
print("Roll NO:",rollno)
print("Name :",name)
print("Maths :",maths)
print("Sci :",sci)
print("Eng :",eng)
if maths>33 and sci>33 and eng>33:
    total=maths+sci+eng
    avg=total/3
    print("total :",total)
    print("Avg:",avg)
    if avg >90:
        print("Grade : A")
    elif avg>70:
        print("Grade : B")
    elif avg>55:
        print("Grade : C")
    else :
        print("Grade : D")
else:
    print("you are failed")

