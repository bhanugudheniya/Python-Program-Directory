s1=input("Enter First String:")
s2=input("Enter Second String:")
pos=s1.find(s2)
if(pos>=0):
	print(f"Substring present at index {pos}")
else:
	print("Substring Not Present")
