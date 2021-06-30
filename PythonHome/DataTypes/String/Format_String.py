# The format() method that is available with the string object is very versatile and powerful in formatting strings.
# Format strings contain curly braces {} as placeholders or replacement fields which get replaced.

# default(implicit) order
default_order = "{}, {} and {}".format('Bhanu', 'India', 'World')
print('\n --- Default Order ---')
print(default_order)

# Order using positional argument
positional_order = "{1}, {0} and {2}".format('Bhanu', 'India', 'World')
print('\n --- Positional Order ---')
print(positional_order)

# Order using keyword argument
keyword_order = "{b}, {i} and {w}".format(b = 'Bhanu', i = "India", w = "World")
print('\n --- Keyword Order ---')
print(keyword_order)