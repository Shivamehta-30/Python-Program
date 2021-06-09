n = int(input("Enter a decimal number"))
i = 0
j = 0
k = n
while (k > 0):
    i = ((k% 2) * (10 ** j)) + i
    k = int(k / 2)
    j+= 1

print("Binary of is:",i)


