n=[5,10,4,8,3,9]
print(f"The List Is {n}")
l=len(n)
for i in range(0,2):
	for j in range(0,l-1):
		if(n[j]>n[j+1]):
			n[j],n[j+1]=n[j+1],n[j]
print(f"The Second Largest Element In The List Is {n[l-2]}")
