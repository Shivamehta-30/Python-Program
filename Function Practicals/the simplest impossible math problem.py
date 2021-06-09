def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3* number + 1)
        return 3 * number + 1
n = input("Give me a number: ")
while n != 1:
    n = collatz(int(n))