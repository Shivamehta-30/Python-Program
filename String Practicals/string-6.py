name = input('Enter a string:')
print(name.title())
for i in name.title():
    if i.istitle():
        print(i,".",end=" ")