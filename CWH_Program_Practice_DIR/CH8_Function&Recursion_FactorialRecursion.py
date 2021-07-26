# n! = 1 * 2 * 3 * 4... *n
# n! = [1 * 2 * 3 * 4... n-1] *n
# n! = n * (n-1)!

# Using loop
"""
n = 0
product = 1
for i in range(n):
	product = product * (i+1)
print(product)
"""

# Using function and loop
"""
def factorial_iter(n):
	product = 1
	for i in range(n):
		product = product * (i+1)
	return product
	
f = factorial_iter(5)
print(f)
"""

# Using Recursion

def factorial_recursive(n):
	if n == 1 or n == 0:    # Base condition which doesn't call the function any further.
		return 1
	return n * factorial_recursive(n-1)     # function calling itself

print(factorial_recursive(4))