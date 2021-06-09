n=int(input("Enter any value "))
rev=0
while (n>0):
        i = n % 10
        rev = rev * 10 + i
        n=n//10

print("Reverse number:",rev)
