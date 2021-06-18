strInput = input("Enter a String : ")
if str == 'x':
	exit()
else:
	newstr = strInput
	print("Removing vowels")
	vowels = ('a', 'e', 'i', 'o', 'u')
	for x in vowels:
		newstr = newstr.replace(x,"")
	print(newstr)