numberType = 12
floatType = 1.2
StringType = "55"

# int to str
str(numberType)
print(str(numberType), type(str(numberType)))

# float to int
int(floatType)
print(int(floatType), type(int(floatType)))

# String to int
# convert_string = int(StringType)
# print(convert_string, type(convert_string))
#				^
#			   /|\  SAME
#			    |

int(StringType)
print(int(StringType), type(int(StringType)))

# int to float
float(numberType)
print(float(numberType), type(float(numberType)))