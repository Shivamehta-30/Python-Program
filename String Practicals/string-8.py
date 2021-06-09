string=input("Enter name")
for i in range(len(string)):
    x=string[i:]+string[:i]
    print(x)
