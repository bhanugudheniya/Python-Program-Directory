# Change VALUE
student = {
	"name" : "bhanu",
	"marks" : 99,
	"subject" : "CS"
}

student["marks"] = 97
print(student)

# Update
student.update({'subject' : 'Computer Science'})
print(student)

# Looping

for i in student:
	print(i, end=", ")

print("\n")

for i in student:
	print(student[i], end=", ")

print("\n")

# Looping using values and keys
for i in student.values():
	print(i, end=", ")

print("\n")

for i in student.keys():
	print(i, end=", ")