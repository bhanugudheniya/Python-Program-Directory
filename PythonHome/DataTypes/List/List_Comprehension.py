"""
List comprehension is an elegant and concise way to create a new list from an existing list in Python.
A list comprehension consists of an expression followed by for statement inside square brackets.
"""

pow2 = [2** x for x in range(10)]
print(pow2)

# is equivalent to below code
'''
pow2 = []
for x in range(10):
   pow2.append(2 ** x)
'''