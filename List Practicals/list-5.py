string=input("Enter any string")
string=list(string)
for value in string:
    print("Removed letter",string.remove(string[0]))
    print(string)
