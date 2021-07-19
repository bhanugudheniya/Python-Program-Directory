student = {
	"name" : "bhanu",
	"marks" : 99,
	"subject" : "CS"
}

# Function Defining
def functionCopy():
	x = student.copy()
	print(x)

def functionGet():
	x = student.get('name')
	print(x)

def functionItems():
	student.items()
	print(student)


# Function Calling
functionCopy()
functionGet()
functionItems()

# other functions are in File - ChangeAndUpdate