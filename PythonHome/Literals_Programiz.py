# Literals
# Literals is a raw data given in a variable or constant.

#Numeric Literals
#   |-> Immutable
#       |-> Integer
#       |-> Float
#       |-> Complex
print("Numeric Literals\n")

a = 0b1010  #Binary Literal
b = 100     #Decimal Literal
c = 0o310   #Octal Literal
d = 0x12c   #Hexadecimal Literal

# Float Literal
float_1 = 10.5
float_2 = 1.5e2

# Complex Literal
x = 3.14j

print(a, b,c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

'''
 - We assigned integer literals into different variables. Here, a is binary literal, b is a decimal literal, c is an octal literal and d is a hexadecimal literal.
 - When we print the variables, all the literals are converted into decimal values.
 - 10.5 and 1.5e2 are floating-point literals. 1.5e2 is expressed with exponential and is equivalent to 1.5 * 102.
 - We assigned a complex literal i.e 3.14j in variable x. Then we use imaginary literal (x.imag) and real literal (x.real) to create imaginary and real parts of complex numbers.
'''

print("\n***********************************\n")

#String Literal
# string literal is a sequence of characters surrounded by quotes. We can use both single, double, or triple quotes for a string.
# And, a character literal is a single character surrounded by single or double quotes.

print("String Literals\n")

strings = "This is Bhanu Gudheniya"
char = "C"
multiline_str = """This is Bhanu Gudheniya World..."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

print("\n***********************************\n")

# Boolean Literal
# A Boolean literal can have any of the two values: True or False.

print("Boolean Literals\n")

x = (1 ==True)
y = (1 == False)
a = True + 4        # True = 1
b = False + 10      # False = 0

print("x is : ", x)
print("y is : ", y)
print("a : ", a)
print("b : ", b)

'''
True represents the value as 1 and False as 0. The value of x is True because 1 is equal to True. And, the value of y is False because 1 is not equal to False.

Similarly, we can use the True and False in numeric expressions as the value. The value of a is 5 because we add True which has a value of 1 with 4. Similarly, b is 10 because
we add the False having value of 0 with 10.
'''

print("\n***********************************\n")

# Special Literals

print("Special Literals\n")

drink = "Available"
food = None

def menu(x):
	if x == drink:
		print(drink)
	else:
		print(food)

menu(drink)
menu(food)

print("\n***********************************\n")

# Literal Collection

print("Literal Collection\n")

fruits = ['apple', 'mango', 'orange']   # List
numbers = (1, 2, 3)                     # Tuple
alphabets = {'a' : 'apple', 'b' : 'ball', 'c' : 'cat'}  # Dictionary with character key
dicInt = {1 : 'abc', 2 : 'pqr', 3 : 'xyz'}    #Dictionary with Integer Key
vowels = {'a', 'e', 'i', 'o', 'u'}  #set

print(fruits)
print(numbers)
print(alphabets)
print(dicInt)
print(vowels)