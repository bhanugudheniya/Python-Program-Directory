print("Enter 1 for Addition \n Enter 2 for Subtraction \n Enter 3 for Multiplication \n Enter 4 for Division \n")
choice = int(input("Enter Your Arithmetic Operation Choice"))

if choice<1 or choice>4:
	print("Invalid Choice")
else:
	num1 = int(input("Enter First Number"))
	num2 = int(input("Enter Second Number"))
	if choice==1:
		print("Addition of two number : ", num1+num2)
	elif choice==2:
		print("Subtraction of two number : ", num1-num2)
	elif choice==3:
		print("Multiplication of two number : ", num1*num2)
	elif choice==4:
		print("Division of two number : ", num1/num2)