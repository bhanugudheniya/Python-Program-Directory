solveValue = 0
numberValue = int(input("Enter a Number\n"))
for i in range(1,4):
	solveValue = solveValue + numberValue**i
print(solveValue)