# Various built-in functions that work with sequence work with strings as well.
# Some of the commonly used ones are enumerate() and len(). The enumerate() function returns an enumerate object.
# It contains the index and value of all the items in the string as pairs. This can be useful for iteration.
# Similarly, len() returns the length (number of characters) of the string.

str = 'cold'

list_enumerate = list(enumerate(str))
print('String Enumerator = ', list_enumerate)

# Character count
print('len(str) = ', len(str))