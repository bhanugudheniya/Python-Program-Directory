friends = ('Bhanu', 'Ashish', 'Shobit', 'Naveen', 'Simran', 'Aditi')

# Method Declaration
def functionCount():
	friends.count(friends)
	print(friends)
	x = friends.count('Ashish')
	print(x)

def functionIndex():
	x = friends.index('Naveen')
	print(x)

# Method Calling
functionCount()     # Returns the number of times a specified value occurs in a tuple
functionIndex()     # Searches the tuple for a specified value and returns the position of where it was found
