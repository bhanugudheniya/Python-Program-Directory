# If we want to print a text like He said, "What's there?", we can neither use single quotes nor double quotes.
# This will result in a SyntaxError as the text itself contains both single and double quotes.
# An escape sequence starts with a backslash and is interpreted differently.

# Using double quotes
print("Hello What's there?")

# Using triple quotes
print('''Hello What's there?''')

# Using Escape \'
print('Hello What\'s there?')