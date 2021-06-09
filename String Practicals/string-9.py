lower = False
upper = False
digit = False
length = False
user="yes"
while user=="yes":
    password = input("Enter any password")
    if len(password)<=8:
        length= True
        for i in password:
            if i.isupper():
                upper = True
            elif i.islower():
                lower= True
            elif i.isdigit():
                digit= True
    if length and upper and lower and digit:
        print("THE PASSWORD IS VALID")
    else:
        print("THE PASSWORD IS INVAILD")
        user = input("Do you want to try again")