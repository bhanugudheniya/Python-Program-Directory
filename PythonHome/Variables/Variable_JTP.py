#Object References
print("Bhanu")

print("***** Check Type *****")
#Type of Varialbe and data
type("Bhanu")

#type number
a=3
print(type(a))

#type string
string="hello"
print(type(string))

#type complex
iota=2+5j
print(type(iota))

print("\n*************************\n")
print("Value Assign to Variable \n")

# Value assign to variable
# There is two variable where values are same so both are pointing to same location
# The variable b refers to the same object that a points to because Python does not create another object.

var1 = 50
var2 = var1
print(var1, var2) #   a ------> | 50 | <-------- b

#Now both variables will refer to the different objects.
alfa = 50
beta = 100
print(alfa, beta)

print("\n*************************\n")
print("Object Identity\n")

a=50
b=a
print(id(a))
print(id(b))
''' 
a and b has same id because the value of both variable is same, this will pointing to same location so the address
will be also same
'''
#Reasssigned variable a
a = 500
print(id(a))

print("\n*************************\n")
print("Variable Names\n")

name = "Bhanu"
age = 23
marks = 100

print(name)
print(age)
print(marks)

# or we print like this also
print(name, age, marks)

print("\n*************************\n")
print("Multiple Assignment\n")

x=y=z=50
print(x)
print(y)
print(z)

# OR

x,y,z = 5,10,15
print(x)
print(y)
print(z)

print("\n*************************\n")

# Python Variable
print("Python Variable\n")
print("1. Local Variable\n")
# Local variables are the variables that declared inside the function and have scope within the function.

# Declaring a function
def add():

    # Defining local variable, scope only within a function
    a = 20
    b = 30
    c = a + b
    print("The sum is : ", c)

#calling a function
add()

'''
if we print value of 'a' outside the function then it gives error
LIKE ::
add()
print(a)

OUTPUT ::
---------
    print(a)
NameError: name 'a' is not defined
'''


# -------

print("\n2. Global Variable\n")
''' 
Global variables can be used throughout the program, and its scope is in the entire program.
A variable declared outside the function is the global variable by default. 
Python provides the global keyword to use global variable inside the function. 
If we don't use the global keyword, the function treats it as a local variable. 
'''

# Declare a variable and initialize it
x = 101

# Global Variable in function
def main():
    # printing a global variable
    global x
    print(x)

    # modifying a global variable
    x = "Welcome to Geek World"
    print(x)

# calling function
main()
print(x)

print("\n*************************\n")
print("Delete a variable\n")
# del Keyword

x = 6
print(x)

# deleting a variable
# del x
# print(x) # give error


print("\n*************************\n")
print("Print Single and multiple variable")

p = 5
q = 6
print(p)
print((q))
print(p,q)

# separate the variables by the comma
print(1,2,3,4,5,6,7,8,9,10)

print("\n*************************\n")
print("Constant\n")
# A constant is a type of variable whose value cannot be changed

import constant     #constant is a file in same directory, which store value of PI, and GRAVITY and this file is imported here
print(constant.PI)
print(constant.GRAVITY)
