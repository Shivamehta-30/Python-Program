n = int(input("Enter any digit: "))
i = n
sum=0
while i>0:
    j = i%10
    sum=sum+j
    i= int(i/10)
print("Sum of digits of",n,"is",sum)

