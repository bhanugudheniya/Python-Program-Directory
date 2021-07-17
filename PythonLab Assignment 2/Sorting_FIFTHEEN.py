l=[]
n=int(input("Enter no. of elements you want in the list:"))
for i in range(0,n):
	a=int(input("Enter a no."))
	l.append(a)
print("The Unsorted List is:")
print(l)
print("The Sorted List is:")
for i in range(0,n-1):
	for j in range(0,n-i-1):
		if(l[j]>l[j+1]):
			l[j],l[j+1]=l[j+1],l[j]
print(l)
