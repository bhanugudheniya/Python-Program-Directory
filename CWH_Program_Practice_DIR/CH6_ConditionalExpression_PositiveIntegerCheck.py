userInput = int(input("Enter Number: "))
if userInput > 0:
	print(userInput, "is a positive integer")
elif userInput < 0:
	print(userInput, "is a negative integer")
else:
	print("Nor Positive and Nor Negative Integer, it's Zero")