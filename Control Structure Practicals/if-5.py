a=int(input("enter number of calls : "))

if a>200 :
    a= a - 200
    print("your bill is :",a*0.40+50*0.50+50*0.60+200)
elif a>150:
     a=a-150
     print("your bill is :",a*0.50+50*0.60 + 200)
elif a>100:
     a=a-100
     print("your bill is :",a*0.60+200)
else:
    print("your bill is : 200")
