matrixInput = int(input("Enter Order of Matrix as same as Identity Value : "))
for i in range(0, matrixInput):
	for j in range(0, matrixInput):
		if i == j:
			print("1", end=" ")
		else:
			print("0", end=" ")
	print()