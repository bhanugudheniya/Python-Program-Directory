# Decimal To Binary Conversion

def convertToBinary(n):
    if n > 1 :
        convertToBinary(n//2)
    print(n % 2, end = '')

# Decimal Number
decimal = int(input("Enter Decimal Number\n"))


convertToBinary(decimal)
print()