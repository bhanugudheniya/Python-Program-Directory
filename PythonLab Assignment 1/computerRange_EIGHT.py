inputNumber = int(input("Enter a number : "))
sum = 0
temp = inputNumber
for i in range(0, inputNumber+1):
	sum = sum+i
print("Sum of all value from 1 to",temp, " is :" , sum)