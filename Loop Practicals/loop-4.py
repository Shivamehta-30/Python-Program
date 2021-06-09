num = int(input("Enter a number to find factorial: "))
factorial = 1
while (num > 0):
        factorial = factorial * num
        num = num - 1
print(factorial)