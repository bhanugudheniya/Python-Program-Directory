userAge = int(input("Enter Your Age: "))
if userAge <= 0 or userAge > 100:
	print("Please Enter Valid Input")
else:
	if userAge < 18:
		print("You are not eligible for voting")
	elif userAge >= 18:
		print("You are eligible for voting")
