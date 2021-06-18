numberValue = int(input("Enter a number: "))
if numberValue == 1:
    for i in range(1, numberValue + 1):
        if numberValue % i == 0:
            break
    print(numberValue, "is divisible by :", i)
else:
    for i in range(2, numberValue+1):
        if numberValue % i == 0:
            break
    print(numberValue, "is divisible by :", i)
