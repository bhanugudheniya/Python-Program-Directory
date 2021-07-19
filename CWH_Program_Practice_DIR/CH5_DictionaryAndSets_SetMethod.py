student = {'Bhanu', 'Ashish', 'Shobit', 'Naveen'}
Person = {'Bhanu', 'Aditi', 'Simran', 'Ashish'}


# Defining Method
def functionAdd():
	student.add('Aditi')
	print(student)


def functionDifference():
	x = student.difference(Person)
	print(x)

def functionDifferenceUpdate():
	student.difference_update(Person)
	print(student)

def functionInsertion():
	x = student.intersection(Person)
	print(x)

def functionIsDisjoint():
	x = student.isdisjoint(Person)
	print(x)

def functionUnion():
	x = student.union(Person)
	print(x)

def functionLength():
	x = len(student)
	print(x)

def functionRemove():
	Person.remove('Simran')
	print(Person)

def functionPop():
	Person.pop()
	print(Person)

# Calling Method
functionAdd()                   # Adds an element to the set
functionDifference()            # Returns a set containing the difference between two or more sets. It gives difference from 1st set
# functionDifferenceUpdate()    # 	Removes the items in this set that are also included in another, specified set
functionInsertion()             # Returns a set, that is the intersection of two or more sets
functionIsDisjoint()            # Returns whether two sets have a intersection or not
functionUnion()                 # Return a set containing the union of sets
functionLength()                # Return Length of set
functionRemove()                # Remove particular value from set
functionPop()                   # Remove random value from set

