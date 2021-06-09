n= int(input('Enter a Binary number: '))
i=0
j=0
while n>0:
    k=n//10
    r=n%10
    i = i + r*2**j
    j +=1
    n=k
print(" Decimal is ", i)