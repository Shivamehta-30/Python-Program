def checkno(user):
    if type(user)!=str:
        print(abs(user),"Its integer")
    else:
        print("Its invaild")
checkno(user=-80.56)