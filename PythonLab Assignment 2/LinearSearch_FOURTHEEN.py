l=[]
n=int(input("Enter no. of elements you want in the list:"))
for i in range(0,n):
	a=int(input("Enter a no."))
	l.append(a)
key=int(input("Enter the key you want to search:"))
for i in range(0,n):
	if(key==l[i]):
		print(f"{key} present at position {i+1}")
