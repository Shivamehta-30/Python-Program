n= int(input("Enter first number: "))
i= int(input("Enter second number: "))
k= 1

while k!=0:
    k =i % n
    if k == 0:
        hcf = n
    else:
        i =n
        n = k

print("HCF is", hcf)