# in this we can access individual character using indexing and range of
# character using slicing.
# OutOfIndex : IndexError
# -1 refers to last item and so on...
# slicing operator - :(colon)

# Accessing string characters
str = 'bhanu'
print('str = ', str)

# first and last character
print('First Character = ', str[0])
print('Last Character = ', str[-1])

# Slicing 2nd to 5th character
print('String[1:3]', str[1:3])  # ha

# Slicing 6th to 2sn last character
print('String[3:-1]', str[3:-1])  # n
