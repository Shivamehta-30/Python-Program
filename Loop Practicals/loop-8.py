n = int(input("Enter a value:"))
i = n
j = 0
while(n > 0):
    dig = n % 10
    j = j * 10 + dig
    n= n // 10
if(i == j):
    print("palindromic number")
else:
    print("is not palindromic number!")