i=0
n=input("Enter a String:")
for char in n:
	if(i % 2 != 0):
		n=n.replace(char, char.upper())
	i = i + 1
print(n)
