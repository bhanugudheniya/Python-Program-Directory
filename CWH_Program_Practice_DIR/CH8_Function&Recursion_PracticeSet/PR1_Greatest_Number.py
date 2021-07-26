def greatestfunction(num1, num2, num3):
	if num1 > num2:
		if num1 > num3:
			return num1
		else:
			return num3
	else:
		if num2 > num3:
			return num2
		else:
			return num3

m1 = greatestfunction(1, 2, 4)
m2 = greatestfunction(2, 8, 1)
m3 = greatestfunction(3, 2, 1)

print("m1 : ", str(m1))
print("m2 : ", m2)
print("m3 : ", m3)