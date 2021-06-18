digitOne = int(input("Enter First Digit : "))
digitTwo = int(input("Enter Second Digit : "))
digitThree = int(input("Enter Third Digit : "))
if digitOne == digitTwo or digitTwo == digitThree or digitThree == digitOne:
	print("Please Enter Different Digits\n")
else:
	Form = [digitOne, digitTwo, digitThree]

	for i in range(0,3):
		for j in range(0, 3):
			for k in range(0, 3):
				# if i != j != k:
					print(Form[i], Form[j], Form[k], end=" ,")