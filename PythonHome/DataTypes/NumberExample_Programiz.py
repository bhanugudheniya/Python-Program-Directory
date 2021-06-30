# Type and isinstance()
# isinstance() used for bool value

a = 5
print(type(a)) # class 'int'

print(type(5.0)) # class 'float'

c = 5 + 3j
print(c + 3) # 8 + 3j

print(isinstance(c, complex)) # true

######################################

# Number System - Binary, Octal, Hexadecimal
print(0b1101011) # 107
print(0xFB + 0b10) # 253(251 + 2)
print(0o15) # 13


#######################################
# Type Conversion
print(int(2.5))
print(1 + 2.0)
print(float(5))
print(complex('3+2j'))

