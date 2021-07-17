stringSet = "Hello World!, This is Bhanu Gudheniya's Computer"

# Methods
def functionCapitalize():   # Convert the First character to upper case
	s1 = stringSet.capitalize()
	print(s1)

def functionCasefold():     # Convert string into lower case
	s1 = stringSet.casefold()
	print(s1)

def functionCenter():       # Returns a centered string with spacing parameter
	s1 = stringSet.center(100)
	print(s1)

def functionCount():        # Returns the number of times a specified value occurs in a string
	s1 = stringSet.count('Bhanu')
	print(s1)

def functionEncode():       # Returns an encoded version of the string
	s1 = stringSet.encode()
	print(s1)

def functionEndsWith():     # Returns true if the string ends with the specified value
	s1 = stringSet.endswith('r')
	print(s1)

def functionFind():         # Searches the string for a specified value and returns the position of where it was found
	s1 = stringSet.find('Bhanu')
	print(s1)

def functionFormat():       # Formats specified values in a string
	s1 = stringSet.format()
	print(s1)

def functionIndex():
	s1 = stringSet.index('Bhanu')
	print(s1)

# Calling Methods
functionCapitalize()
functionCasefold()
functionCenter()
functionCount()
functionEncode()
functionEndsWith()
functionFind()
functionFormat()
functionIndex()

'''
There are Some Other Functions : https://www.w3schools.com/python/python_ref_string.asp
'''