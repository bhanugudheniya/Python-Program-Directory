
stringInput = input('Enter a string: ')
lower = upper = digit = 0 #alphas

for ch in stringInput:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    # elif ch.isalpha():
    #     alphas += 1

print('The number of uppercase letters:', upper)
print('The number of lowercase letters:', lower)
print('The number of digits:', digit)
print('Total alphabets are : ', len(stringInput))
# print('The number of whitespace characters:', number)