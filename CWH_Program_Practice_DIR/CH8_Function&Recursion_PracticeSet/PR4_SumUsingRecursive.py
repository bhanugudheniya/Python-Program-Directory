def sumVal(n):
	if n <= 1:
		return n
	return n + sumVal(n-1)

print(sumVal(5))