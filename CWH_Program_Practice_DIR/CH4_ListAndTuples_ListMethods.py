friends = ['Bhanu', 'Ashish', 'Shobit', 'Naveen', 'Simran', 'Aditi']
newFriends = 'Dushyant'
kukasFriends = ['Rohit', 'Prashant']

# Method Declaration
def functionAppend():
	friends.append(newFriends)
	print(friends)

def functionClear():
	friends.clear()
	print(friends)

def functionCopy():
	x = friends.copy()
	print(x)

def functionCount():
	x = friends.count("Bhanu")
	print(x)

def functionExtend():
	friends.extend(kukasFriends)
	print(friends)

def functionIndex():
	x = friends.index("Dushyant")
	print(x)

def functionInsert():
	friends.insert(5, "Shubham")
	print(friends)

def functionPop():
	friends.pop(4)
	print(friends)

def functionRemove():
	friends.remove('Aditi')
	print(friends)

def functionReverse():
	friends.reverse()
	print(friends)

def functionSort():
	friends.sort()
	print(friends)


# Method Calling
functionAppend()        # Adds an element at the end of the list
# functionClear()       # Removes all the elements from the list
functionCopy()          # Returns a copy of the list
functionCount()         # Returns the number of elements with the specified value
functionExtend()        # Add the elements of a list (or any iterable), to the end of the current list
functionIndex()         # Returns the index of the first element with the specified value
functionInsert()        # Adds an element at the specified position
functionPop()           # Removes the element at the specified position
functionRemove()        # Removes the first item with the specified value
functionReverse()       # Reverses the order of the list
functionSort()          # Sorts the list

