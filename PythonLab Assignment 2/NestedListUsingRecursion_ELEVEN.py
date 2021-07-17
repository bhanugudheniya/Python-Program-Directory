def sum1(lst):
	total = 0
	for element in lst:
		if (type(element) == type([])):
			total = total + sum1(element)
		else:
			total = total + element
		return total
a=[[1,2],[3,4]]
print("List is:")
print(a)
print( "Sum is:",sum1(a))
