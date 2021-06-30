"""
In python every created object identifies uniquely in python.
It provides the guaranteed that no two objects will have the same identifiers.
The build-in id() function, is used to identify the object identifiers.
"""

a = 50
b = a
c = 100

print(id(a))
print(id(b))
print(id(c))
