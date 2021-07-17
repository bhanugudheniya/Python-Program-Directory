L=[]
K=[]
n=int(input("Enter Number of elements in a list that you want to insert:"))
for i in range(n):
	x=input()
	L.append(x)
for i in L:
	y=L.count(i)
	if(y%2!=0):
		if(i not in K):
			K.append(i)
			print("The element which is occurring odd number of times is:",i)
if(K==[]):
	print("There are no elements which occur odd number of times")
