list = [-11,0,11, 22, 33, 44, 55]
print("List Before removing ODD numbers and Negative Numbers")
print(list)
for el in list:
	if(el%2 != 0 or el<0): list.remove(el)
# print list after removing ODD elements
print("list after removing ODD numbers and Negative Numbers:")
print(list)
