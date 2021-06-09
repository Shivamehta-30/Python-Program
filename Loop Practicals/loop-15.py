number=sum=0
k=int(input("Enter the value"))
for i in range(0,k):
    number=i
    sum=0
    while number>0:
        digit = number%10
        sum=sum+pow(digit,3)
        number= int(number/10)
    if i==sum:
        print(i)