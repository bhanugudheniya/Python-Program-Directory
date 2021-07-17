s1=input("Enter First String:")
s2=input("Enter Second String:")
s1=list(s1)
s2=list(s2)
for i in range(len(s1)):
	ctr=0
	for j in range(len(s2)):
		if(s1[i]==s2[j]):
			ctr+=1
		if(ctr==0):
			print(s1[i],end=" ")
