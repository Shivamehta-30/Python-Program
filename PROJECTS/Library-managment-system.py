op=1
lib_list=[]
title=["Id","Name:","Book name:","Date of issue","Date of return","Number of days","Price"]
while op!=5 :
    print("\t\t Library Managment")
    print("\t\t 1.Entry: ")
    print("\t\t 2.View: ")
    print("\t\t 3.Search: ")
    print("\t\t 4.Search by book: ")
    print("\t\t 5.Exit: ")

    op=int(input("Enter your option :"))
    if op==1:
        user='yes'
        while user=="yes":
            customer=[]
            customer.append(int(input("Enter customer id:")))
            customer.append(input("Enter customer name:"))
            customer.append(input("What is book name?"))
            customer.append(input("What is the date of issue?"))
            customer.append(input("What is return of date?"))
            customer.append(int(input("How many days you want book for rent")))
            price=customer[5]*50
            customer.append(price)
            user = input("Do you want to add any data in system?????")
            lib_list.append(customer)
    elif op==2:
        for customer in lib_list:
            for t, value in zip(title[0:], customer[0:]):
                print(t, value)
    elif op==3:
        c_id = int(input("Enter customer id for search?:"))
        for customer in lib_list:
            if c_id == customer[0]:
                for t, value in zip(title[0:], customer[0:]):
                    print(t, value)
    elif op==4:
        c_book = (input("Enter customer book name for search?:"))
        for customer in lib_list:
            if c_book == customer[2]:
                for t, value in zip(title[0:], customer[0:]):
                    print(t, value)
    elif op == 5:
        print("you are exited ")
    else:
        print("wrong option selected try again !!")