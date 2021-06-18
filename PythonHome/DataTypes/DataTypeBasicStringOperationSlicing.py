s = 'Hello World'
print("s[4] =", s[4])
print("s[6:11] =", s[6:11])  #--> [6:11] - [n:m]; m = print value - 1
# string indexing starts with zero
#if we want to slicing is perform on string at [6:11] it means string start from 6th index and end on 10th index or
# print till 10th index


# s[5]='d'
#   ^
# Traceback (most recent call last):
# File "<string>", line 11, in <module>
# TypeError: 'str' object does not support item assignment

#############################################################

str1 = "hello bhanu gudheniya"
str2 = "how are you"

print(str1[0:2]) #printing first two character using slice operator
print(str1[4]) #printing 4th character of the string
print(str1*2) #printing the string twice
print(str1 + str2) #printing the concatenation of str1 and str2
