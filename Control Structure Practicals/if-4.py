year=int(input("Enter any year"))
if  year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"Is a leap year")
        else:
            print(year,"Is not a leap year")
    else:
        print(year,"Is leap year")
else:
    print(year,"Is not leap year")
#1992
#2000
#1900
#1995