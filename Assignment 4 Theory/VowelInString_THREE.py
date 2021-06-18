strInput = input("Enter a string : ")
vowel = 0
for loop in strInput:
	if loop == 'a' or loop == 'e' or loop == 'i' or loop == 'o' or loop == 'u':
		vowel = vowel + 1
print("Total Vowels are :",vowel)
