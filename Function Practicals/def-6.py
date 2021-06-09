def cube(user):
    num=user**(3)
    print("cube=",num)
def condition(user):
    if user%3==0:
        cube(user)
    else:
        print(cube(user),"Not divide by 3")
condition(user=int(input("Enter value")))