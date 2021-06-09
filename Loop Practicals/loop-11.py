n= int(input("Enter any Number: "))
j= 0
i = 2

while (i <= n // 2):
    if (n % i == 0):
        j = j + 1
    i = i + 1

if (j == 0 and n!=1):
    print("is a Prime Number",n)
else:
    print("is not a Prime Number",n)
