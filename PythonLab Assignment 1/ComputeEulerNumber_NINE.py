numberInput = int(input('Enter a number: '))
fact = 1
sum = 1
for i in range(1, numberInput+1):
    fact = fact * i
    sum = sum + 1/fact
print("Sum of the Euler's Number :", sum)
