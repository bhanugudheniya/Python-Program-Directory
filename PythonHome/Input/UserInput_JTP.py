name = input("Enter name of student : ")
print("Student name is : ", name)

# 'name' is variable which store value are stored by user
# 'input()' is function which is helps to take user input and string are written in this which is as it is show on screen

# ---------------------------------------------------------------------------------------------------------------------------- #

# --> By default the 'input()' function takes the string input but what if we want to take other data types as an input
# --> If we want to take input as an integer number, we need to typecast the input() function an integer

a = int(input("Enter First Number = "))
b = int(input("Enter Second Number = "))

print(a+b)