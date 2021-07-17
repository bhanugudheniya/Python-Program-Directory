b=[]
a=input("Enter a String:")
a=list(a)
l=len(a)
for i in range(l-1,-1,-1):
	b.append(a[i])
if(str(a)==str(b)):
	print("Palindrome")
else:
	print("Not a Palindrome")
