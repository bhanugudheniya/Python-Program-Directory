student = {
	"name" : "bhanu",
	"marks" : 99,
	"subject" : "CS",
	# "marks" : 98    # always print last updated value
}

print(student)      # print whole dictionary
print(student["name"])  # print value of key "name"
print(len(student))     # print dictionary length
print(type(student))    # data types

# Access Dictionary
x = student.get("marks")        # get by key
print(x)

y = student.keys()              # get all keys
print(y)

val = student.values()          # print all values
print(val)