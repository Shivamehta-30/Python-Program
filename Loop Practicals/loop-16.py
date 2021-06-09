n = int(input("Enter number of terms: "))
a = 0
b = 1
i = 0
print("Fibonacci sequence:")
while (i < n):
    print(a,end=" ")
    sum = a + b
    a = b
    b = sum
    i += 1
