user='yes'
i=0
j=0
k=0
while user=='yes':
    n=int(input("Enter any value :"))
    if n > 0:
         i = i + 1
    elif n < 0:
        j = j + 1
    else:
          k = k + 1
    user = input("Do you want to add any value:")

print("Positive values are:",i)
print("Negative values are:",j)
print("zeros value are:",k)
