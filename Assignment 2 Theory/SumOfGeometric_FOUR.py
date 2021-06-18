# S=a+ar+ar2+ar3+ar4+……. +arn

def sumOfGeometric(n):
    # base case
    if n == 0:
        return 1
    return 1 / pow(2, n) + sumOfGeometric(n - 1)

# n = 5
number = int(input("Enter Number\n"))

print(sumOfGeometric(number))
