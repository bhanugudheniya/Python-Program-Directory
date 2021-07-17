friends = ['Bhanu', 'Ashish', 'Shobit', 'Naveen', 'Simran', 'Aditi']
newFriends = 'Dushyant'
kukasFriends = ['Rohit', 'Prashant']

# Method Declaration
def functionLoop():
	print("Loop Running : ")
	for i in friends:
		print(i, end=", ")

def functionIndexLoop():
	print("\n\nIndex Looping: ")
	for i in range(len(friends)):
		print(friends[i], end=", ")

def functionWhileLoop():
	i = 0
	print("\n\nWhile Looping: ")
	while i < len(friends):
		print(friends[i], end=", ")
		i = i + 1

# Method Calling
functionLoop()
functionIndexLoop()
functionWhileLoop()