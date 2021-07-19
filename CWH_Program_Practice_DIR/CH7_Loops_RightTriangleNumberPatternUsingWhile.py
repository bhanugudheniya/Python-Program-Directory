n = int(input("Enter Row no : "))

i = 1
num = 1
while i <= n:
	j = 1
	while j <= i:
		print(num, end=" ")
		j += 1
		num += 1
	print()
	i += 1