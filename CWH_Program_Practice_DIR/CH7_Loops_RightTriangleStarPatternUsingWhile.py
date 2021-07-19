n = int(input("Enter Row no : "))

i = 1
while i <= n:
	j = 1
	while j <= i:
		print("*", end=" ")
		j += 1  #increase column
	print()     #print next line
	i += 1      #increase row