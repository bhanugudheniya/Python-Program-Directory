LowerValue = int(input("Enter Lower Value: "))
UpperValue = int(input("Enter Upper Value: "))
check = int(input("Enter number to check divisibility: "))
for loop in range(LowerValue, UpperValue+1):
    if loop % check == 0:
        print(loop, end=" ")