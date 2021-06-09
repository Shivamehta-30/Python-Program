msg = input("Enter string")
lower = 0
upper = 0
space = 0
digit = 0

for ch in msg:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    elif ch == ' ':
        space += 1

print('The number of uppercase letters:', upper)
print('The number of lowercase letters:', lower)
print('The number of whitespace characters:', space)
print('The number of digit ', digit)
