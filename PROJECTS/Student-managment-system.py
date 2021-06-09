op=1
std_student_list={1:{'A':[],"B":[],"C":[]},2:{'A':[],"B":[],"C":[]}}
#div_student_list=
title=["Roll No","Name:","Maths:","Sci:","Eng:","Phy:"]
while op!=4 :
    print("\t\t Student Info")
    print("\t\t 1.Entry")
    print("\t\t 2.View ")
    print("\t\t 3.Search")
    print("\t\t 4.top 3 in Maths")
    print("\t\t 5.Exit ")

    op=int(input("Enter your option :"))

    if op==1:
        print("\t\tEntry")
        op1 = "yes"
        while op1 == "yes":
            for keys in std_student_list.keys():
                print("press ",keys,"for std",keys)
            std=int(input("Enter std"))
            if std not in std_student_list:
                print("invalid option entered ")
            else:
                for keys in std_student_list[std]:
                    print("Press",keys,"for",keys)
                div=input("Enter your option :").upper()
                if div not in std_student_list[std]:
                    print("invalid option entered ")
                student={}
                student.__setitem__(title[0],int(input("Enter Roll No:")))
                student.__setitem__(title[1],input("Enter Name :"))
                for t in title[2:]:
                    marks=int(input(" Enter " +t+ " Marks "))
                    while not (0<=marks<=100):
                        print("invalid marks")
                        marks=int(input("Enter" +t+ "Marks:"))
                    student[t]=marks
                std_student_list[std][div].append(student)
            op1=input("do you want to add another student (yes/no)?:")
    elif op==2:
        for keys in std_student_list.keys():
            print("press ", keys, "for division", keys)
        std = int(input("Enter std"))
        if std not in std_student_list:
            print("invalid option entered ")
        else:
            for keys in std_student_list[std].keys():
                print("press ",keys, " for division ", keys)
            div = input("Enter your option :").upper()
            for student in std_student_list[std][div]:
                is_pass=True
                for t,value in student.items() :
                    print(t,value)
                    if t != title[0] and t!=title[1]:
                        if value<=33:
                            is_pass=False
                if is_pass==True:
                    total=sum(list(student.values())[2:])
                    avg=total/len(list(student.values())[2:])
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
    elif op==3:
        for keys in std_student_list.keys():
            print("press ", keys, "for division", keys)
        std = int(input("Enter std"))
        if std not in std_student_list:
            print("invalid option entered ")
        else:
            for keys in std_student_list[std].keys():
                print("press ", keys, " for division ", keys)
        div = input("Enter your option :").upper()
        s_rollno=int(input("Enter rollno for search:"))
        for student in std_student_list[std][div]:
            if s_rollno==student[title[0]]:
                is_pass = True;
                for t, value in student.items():
                    print(t, value)
                    if t != title[0] and t != title[1]:
                        if value <= 33:
                            is_pass = False;

                if is_pass == True:
                    total = sum(list(student.values())[2:])
                    avg = total / len(list(student.values())[2:])
                    print("total :", total)
                    print("Avg:", avg)
                    if avg > 90:
                        print("Grade : A")
                    elif avg > 70:
                        print("Grade : B")
                    elif avg > 55:
                        print("Grade : C")
                    else:
                        print("Grade : D")
                else:
                    print("you are failed")
    elif op==4:
        print("you are exited ")
    else :
        print("wrong option selected try again !!")