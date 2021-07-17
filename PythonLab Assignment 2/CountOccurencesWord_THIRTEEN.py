count=0
with open("file1.txt","r") as f:
	s=input("Enter a String:")
	for i in f:
		i.find(s)
		count+=1
	print(f"{s} occurred {count} times")
