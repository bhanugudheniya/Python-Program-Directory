numberValue = int(input("Enter a number : "))
sum = 0
copy = numberValue
while numberValue > 0:
	temp = numberValue % 10
	sum = sum + temp
	numberValue = numberValue//10
print("Sum of digit : ", copy, "is : ", sum)